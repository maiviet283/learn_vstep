# -*- coding: utf-8 -*-
"""Nap toan bo hoc lieu VSTEP vao database. Chay: python manage.py seed_data"""
from django.core.management.base import BaseCommand
from django.db import transaction

from learning.data.grammar_1 import UNITS_1
from learning.data.grammar_2 import UNITS_2
from learning.data.grammar_3 import UNITS_3
from learning.data.grammar_4 import UNITS_4
from learning.data.grammar_extra1 import EXTRA_QUESTIONS_1
from learning.data.grammar_extra2 import EXTRA_QUESTIONS_2
from learning.data.listening import TRACKS
from learning.data.listening_2 import TRACKS_2
from learning.data.reading import PASSAGES
from learning.data.reading_2 import PASSAGES_2
from learning.data.skills import SPEAKING_LESSONS, WRITING_LESSONS
from learning.data.vocab_1 import TOPICS_1
from learning.data.vocab_2 import TOPICS_2
from learning.data.vocab_3 import TOPICS_3
from learning.data.vocab_4 import TOPICS_4
from learning.data.vocab_5 import EXTRA_WORDS
from learning.models import (GrammarLesson, ListeningTrack, Question,
                             ReadingPassage, SpeakingLesson, Unit, VocabTopic,
                             VocabWord, WritingLesson)


class Command(BaseCommand):
    help = 'Seed VSTEP learning content (grammar, vocab, reading, listening, writing, speaking).'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write('Xoa du lieu cu...')
        Question.objects.all().delete()
        GrammarLesson.objects.all().delete()
        Unit.objects.all().delete()
        VocabWord.objects.all().delete()
        VocabTopic.objects.all().delete()
        ReadingPassage.objects.all().delete()
        ListeningTrack.objects.all().delete()
        WritingLesson.objects.all().delete()
        SpeakingLesson.objects.all().delete()

        # --- Ngu phap ---
        extra_questions = {**EXTRA_QUESTIONS_1, **EXTRA_QUESTIONS_2}
        for u in UNITS_1 + UNITS_2 + UNITS_3 + UNITS_4:
            unit = Unit.objects.create(order=u['order'], title=u['title'],
                                       title_vi=u['title_vi'],
                                       description=u['description'], level=u['level'])
            GrammarLesson.objects.create(unit=unit, content=u['content'])
            questions = list(u['questions']) + list(extra_questions.get(u['order'], []))
            for (text, a, b, c, d, correct, expl) in questions:
                Question.objects.create(skill='grammar', unit=unit, text=text,
                                        option_a=a, option_b=b, option_c=c, option_d=d,
                                        correct=correct, explanation=expl, level=u['level'])
        self.stdout.write(self.style.SUCCESS(
            f'  {Unit.objects.count()} units, {Question.objects.filter(skill="grammar").count()} cau ngu phap'))

        # --- Tu vung ---
        for i, t in enumerate(TOPICS_1 + TOPICS_2 + TOPICS_3 + TOPICS_4, start=1):
            topic = VocabTopic.objects.create(name=t['name'], name_vi=t['name_vi'],
                                              icon=t['icon'], description=t['description'],
                                              order=i)
            words = list(t['words']) + list(EXTRA_WORDS.get(t['name'], []))
            for (word, pos, ipa, meaning, ex_en, ex_vi, level) in words:
                VocabWord.objects.create(topic=topic, word=word, pos=pos, ipa=ipa,
                                         meaning_vi=meaning, example_en=ex_en,
                                         example_vi=ex_vi, level=level)
        self.stdout.write(self.style.SUCCESS(
            f'  {VocabTopic.objects.count()} chu de, {VocabWord.objects.count()} tu vung'))

        # --- Doc hieu ---
        for p in PASSAGES + PASSAGES_2:
            passage = ReadingPassage.objects.create(title=p['title'], level=p['level'],
                                                    content=p['content'],
                                                    translation_vi=p['translation_vi'],
                                                    order=p['order'])
            for (text, a, b, c, d, correct, expl) in p['questions']:
                Question.objects.create(skill='reading', passage=passage, text=text,
                                        option_a=a, option_b=b, option_c=c, option_d=d,
                                        correct=correct, explanation=expl, level=p['level'])
        self.stdout.write(self.style.SUCCESS(
            f'  {ReadingPassage.objects.count()} bai doc, {Question.objects.filter(skill="reading").count()} cau hoi'))

        # --- Nghe hieu ---
        for t in TRACKS + TRACKS_2:
            track = ListeningTrack.objects.create(title=t['title'], level=t['level'],
                                                  transcript=t['transcript'],
                                                  translation_vi=t['translation_vi'],
                                                  order=t['order'])
            for (text, a, b, c, d, correct, expl) in t['questions']:
                Question.objects.create(skill='listening', track=track, text=text,
                                        option_a=a, option_b=b, option_c=c, option_d=d,
                                        correct=correct, explanation=expl, level=t['level'])
        self.stdout.write(self.style.SUCCESS(
            f'  {ListeningTrack.objects.count()} bai nghe, {Question.objects.filter(skill="listening").count()} cau hoi'))

        # --- Viet & Noi ---
        for w in WRITING_LESSONS:
            WritingLesson.objects.create(**w)
        for s in SPEAKING_LESSONS:
            SpeakingLesson.objects.create(**s)
        self.stdout.write(self.style.SUCCESS(
            f'  {WritingLesson.objects.count()} bai viet, {SpeakingLesson.objects.count()} bai noi'))

        self.stdout.write(self.style.SUCCESS(
            f'HOAN TAT! Tong cong {Question.objects.count()} cau hoi trong ngan hang de.'))
