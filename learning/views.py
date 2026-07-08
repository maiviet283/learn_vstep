import random

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

from .models import (ListeningTrack, Question, QuizAttempt, ReadingPassage,
                     SpeakingLesson, Unit, VocabTopic, VocabWord,
                     WordProgress, WritingLesson)


def home(request):
    stats = {
        'units': Unit.objects.count(),
        'words': VocabWord.objects.count(),
        'questions': Question.objects.count(),
        'passages': ReadingPassage.objects.count() + ListeningTrack.objects.count(),
    }
    recent = None
    known_words = 0
    if request.user.is_authenticated:
        recent = request.user.attempts.all()[:5]
        known_words = request.user.word_progress.filter(known=True).count()
    return render(request, 'learning/home.html', {
        'stats': stats, 'recent': recent, 'known_words': known_words,
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'learning/register.html', {'form': form})


# ---------- Cham diem chung ----------

def _grade(request, questions):
    """Cham cac cau hoi Question tu POST (name='q<id>'). Tra ve (results, score)."""
    results, score = [], 0
    for q in questions:
        chosen = request.POST.get(f'q{q.id}', '')
        ok = chosen == q.correct
        if ok:
            score += 1
        results.append({
            'q': q, 'chosen': chosen,
            'chosen_text': dict(q.options()).get(chosen, '(chưa chọn)'),
            'ok': ok,
        })
    return results, score


def _pct(score, total):
    return round(score * 100 / total) if total else 0


def _save_attempt(request, kind, label, score, total):
    if request.user.is_authenticated and total:
        QuizAttempt.objects.create(user=request.user, kind=kind, label=label,
                                   score=score, total=total)


# ---------- Ngu phap ----------

def grammar_list(request):
    units = Unit.objects.annotate(n_questions=Count('questions'))
    return render(request, 'learning/grammar_list.html', {'units': units})


def grammar_detail(request, pk):
    unit = get_object_or_404(Unit.objects.select_related('lesson'), pk=pk)
    prev_unit = Unit.objects.filter(order__lt=unit.order).last()
    next_unit = Unit.objects.filter(order__gt=unit.order).first()
    return render(request, 'learning/grammar_detail.html', {
        'unit': unit, 'prev_unit': prev_unit, 'next_unit': next_unit,
    })


def grammar_quiz(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == 'POST':
        ids = request.POST.getlist('qid')
        questions = list(Question.objects.filter(id__in=ids, unit=unit))
        questions.sort(key=lambda q: ids.index(str(q.id)))
        results, score = _grade(request, questions)
        _save_attempt(request, 'grammar', f'Ngữ pháp – Unit {unit.order}: {unit.title}',
                      score, len(questions))
        return render(request, 'learning/quiz_result.html', {
            'title': f'Kết quả – Unit {unit.order}: {unit.title}',
            'results': results, 'score': score, 'total': len(questions),
            'percent': _pct(score, len(questions)),
            'back_url': 'grammar_detail', 'back_pk': unit.pk,
        })
    questions = unit.questions.all()
    return render(request, 'learning/quiz.html', {
        'title': f'Luyện tập – Unit {unit.order}: {unit.title}',
        'subtitle': unit.title_vi,
        'questions': questions,
    })


# ---------- Tu vung ----------

def vocab_topics(request):
    topics = VocabTopic.objects.annotate(n_words=Count('words'))
    return render(request, 'learning/vocab_topics.html', {'topics': topics})


@ensure_csrf_cookie
def vocab_detail(request, pk):
    topic = get_object_or_404(VocabTopic, pk=pk)
    words = topic.words.all()
    known_ids = set()
    if request.user.is_authenticated:
        known_ids = set(request.user.word_progress.filter(
            known=True, word__topic=topic).values_list('word_id', flat=True))
    return render(request, 'learning/vocab_detail.html', {
        'topic': topic, 'words': words, 'known_ids': known_ids,
    })


def flashcards(request, pk):
    topic = get_object_or_404(VocabTopic, pk=pk)
    words = list(topic.words.all())
    random.shuffle(words)
    return render(request, 'learning/flashcards.html', {'topic': topic, 'words': words})


@login_required
@require_POST
def mark_word(request, pk):
    word = get_object_or_404(VocabWord, pk=pk)
    known = request.POST.get('known') == '1'
    WordProgress.objects.update_or_create(user=request.user, word=word,
                                          defaults={'known': known})
    return JsonResponse({'ok': True, 'known': known})


def _vocab_mcq(topic, words, n=10):
    """Sinh cau hoi trac nghiem tu vung: chon nghia dung cua tu."""
    pool = list(words)
    random.shuffle(pool)
    quiz = []
    all_meanings = [w.meaning_vi for w in words]
    for w in pool[:n]:
        distractors = random.sample([m for m in all_meanings if m != w.meaning_vi],
                                    k=min(3, len(all_meanings) - 1))
        opts = distractors + [w.meaning_vi]
        random.shuffle(opts)
        quiz.append({'word': w, 'options': opts})
    return quiz


def vocab_quiz(request, pk):
    topic = get_object_or_404(VocabTopic, pk=pk)
    words = list(topic.words.all())
    if request.method == 'POST':
        ids = request.POST.getlist('wid')
        results, score = [], 0
        for wid in ids:
            w = next((x for x in words if str(x.id) == wid), None)
            if not w:
                continue
            chosen = request.POST.get(f'w{wid}', '(chưa chọn)')
            ok = chosen == w.meaning_vi
            if ok:
                score += 1
            results.append({'word': w, 'chosen': chosen, 'ok': ok})
        _save_attempt(request, 'vocab', f'Từ vựng – {topic.name_vi}', score, len(results))
        return render(request, 'learning/vocab_quiz_result.html', {
            'topic': topic, 'results': results, 'score': score, 'total': len(results),
            'percent': _pct(score, len(results)),
        })
    if len(words) < 4:
        return redirect('vocab_detail', pk=pk)
    quiz = _vocab_mcq(topic, words)
    return render(request, 'learning/vocab_quiz.html', {'topic': topic, 'quiz': quiz})


# ---------- Doc hieu ----------

def reading_list(request):
    passages = ReadingPassage.objects.annotate(n_questions=Count('questions'))
    return render(request, 'learning/reading_list.html', {'passages': passages})


def reading_detail(request, pk):
    passage = get_object_or_404(ReadingPassage, pk=pk)
    questions = passage.questions.all()
    if request.method == 'POST':
        results, score = _grade(request, questions)
        _save_attempt(request, 'reading', f'Đọc hiểu – {passage.title}', score, len(questions))
        return render(request, 'learning/reading_detail.html', {
            'passage': passage, 'questions': questions,
            'results': results, 'score': score, 'total': len(questions),
            'percent': _pct(score, len(questions)),
        })
    return render(request, 'learning/reading_detail.html', {
        'passage': passage, 'questions': questions,
    })


# ---------- Nghe hieu ----------

def listening_list(request):
    tracks = ListeningTrack.objects.annotate(n_questions=Count('questions'))
    return render(request, 'learning/listening_list.html', {'tracks': tracks})


def listening_detail(request, pk):
    track = get_object_or_404(ListeningTrack, pk=pk)
    questions = track.questions.all()
    if request.method == 'POST':
        results, score = _grade(request, questions)
        _save_attempt(request, 'listening', f'Nghe hiểu – {track.title}', score, len(questions))
        return render(request, 'learning/listening_detail.html', {
            'track': track, 'questions': questions,
            'results': results, 'score': score, 'total': len(questions),
            'percent': _pct(score, len(questions)),
        })
    return render(request, 'learning/listening_detail.html', {
        'track': track, 'questions': questions,
    })


# ---------- Viet & Noi ----------

def writing(request):
    lessons = WritingLesson.objects.all()
    return render(request, 'learning/writing.html', {'lessons': lessons})


def speaking(request):
    lessons = SpeakingLesson.objects.all()
    return render(request, 'learning/speaking.html', {'lessons': lessons})


# ---------- Thi thu ----------

MOCK_N_GRAMMAR = 25
MOCK_N_VOCAB = 10
MOCK_N_PASSAGES = 2
MOCK_MINUTES = 40


def mock_test_start(request):
    return render(request, 'learning/mock_start.html', {
        'n_grammar': MOCK_N_GRAMMAR, 'n_vocab': MOCK_N_VOCAB,
        'n_passages': MOCK_N_PASSAGES, 'n_reading': MOCK_N_PASSAGES * 5,
        'minutes': MOCK_MINUTES,
    })


def mock_test(request):
    if request.method == 'POST':
        qids = request.POST.getlist('qid')
        questions = list(Question.objects.filter(id__in=qids))
        questions.sort(key=lambda q: qids.index(str(q.id)))
        results, score = _grade(request, questions)

        wids = request.POST.getlist('wid')
        vocab_results = []
        words = VocabWord.objects.filter(id__in=wids)
        wmap = {str(w.id): w for w in words}
        for wid in wids:
            w = wmap.get(wid)
            if not w:
                continue
            chosen = request.POST.get(f'w{wid}', '(chưa chọn)')
            ok = chosen == w.meaning_vi
            if ok:
                score += 1
            vocab_results.append({'word': w, 'chosen': chosen, 'ok': ok})

        total = len(results) + len(vocab_results)
        _save_attempt(request, 'mock', 'Thi thử tổng hợp', score, total)
        return render(request, 'learning/mock_result.html', {
            'results': results, 'vocab_results': vocab_results,
            'score': score, 'total': total, 'percent': _pct(score, total),
        })

    grammar_qs = list(Question.objects.filter(skill='grammar'))
    random.shuffle(grammar_qs)
    grammar_qs = grammar_qs[:MOCK_N_GRAMMAR]

    passages = list(ReadingPassage.objects.order_by('?')[:MOCK_N_PASSAGES])
    reading_sections = [{'passage': p, 'questions': list(p.questions.all())}
                        for p in passages]

    all_words = list(VocabWord.objects.all())
    vocab_quiz_items = []
    if len(all_words) >= 4:
        picked = random.sample(all_words, min(MOCK_N_VOCAB, len(all_words)))
        meanings = [w.meaning_vi for w in all_words]
        for w in picked:
            distractors = random.sample([m for m in meanings if m != w.meaning_vi], 3)
            opts = distractors + [w.meaning_vi]
            random.shuffle(opts)
            vocab_quiz_items.append({'word': w, 'options': opts})

    return render(request, 'learning/mock_test.html', {
        'grammar_qs': grammar_qs, 'reading_sections': reading_sections,
        'vocab_quiz': vocab_quiz_items, 'minutes': MOCK_MINUTES,
    })


# ---------- Tien do ----------

@login_required
def progress(request):
    attempts = request.user.attempts.all()[:50]
    known = request.user.word_progress.filter(known=True).count()
    total_words = VocabWord.objects.count()
    by_kind = (request.user.attempts.values('kind')
               .annotate(n=Count('id')))
    return render(request, 'learning/progress.html', {
        'attempts': attempts, 'known': known, 'total_words': total_words,
        'by_kind': by_kind,
    })
