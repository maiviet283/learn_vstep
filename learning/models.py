from django.conf import settings
from django.db import models


class Unit(models.Model):
    """Mot unit ngu phap theo giao trinh Destination B1/B2."""
    order = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=200)
    title_vi = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    level = models.CharField(max_length=5, default='B1')  # B1 / B2

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'Unit {self.order}: {self.title}'


class GrammarLesson(models.Model):
    """Ly thuyet cua mot unit (HTML, giai thich tieng Viet + vi du song ngu)."""
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE, related_name='lesson')
    content = models.TextField()

    def __str__(self):
        return f'Lesson: {self.unit.title}'


class VocabTopic(models.Model):
    name = models.CharField(max_length=100)
    name_vi = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, default='📚')
    description = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class VocabWord(models.Model):
    topic = models.ForeignKey(VocabTopic, on_delete=models.CASCADE, related_name='words')
    word = models.CharField(max_length=100)
    pos = models.CharField(max_length=30, blank=True)   # (n), (v), (adj)...
    ipa = models.CharField(max_length=100, blank=True)
    meaning_vi = models.CharField(max_length=300)
    example_en = models.TextField(blank=True)
    example_vi = models.TextField(blank=True)
    level = models.CharField(max_length=5, default='B1')

    class Meta:
        ordering = ['word']

    def __str__(self):
        return self.word


class ReadingPassage(models.Model):
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=5, default='B1')
    content = models.TextField()
    translation_vi = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ListeningTrack(models.Model):
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=5, default='B1')
    transcript = models.TextField()
    translation_vi = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Question(models.Model):
    SKILLS = [
        ('grammar', 'Ngữ pháp'),
        ('vocab', 'Từ vựng'),
        ('reading', 'Đọc hiểu'),
        ('listening', 'Nghe hiểu'),
    ]
    skill = models.CharField(max_length=10, choices=SKILLS)
    unit = models.ForeignKey(Unit, null=True, blank=True, on_delete=models.CASCADE, related_name='questions')
    topic = models.ForeignKey(VocabTopic, null=True, blank=True, on_delete=models.CASCADE, related_name='questions')
    passage = models.ForeignKey(ReadingPassage, null=True, blank=True, on_delete=models.CASCADE, related_name='questions')
    track = models.ForeignKey(ListeningTrack, null=True, blank=True, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    option_a = models.CharField(max_length=300)
    option_b = models.CharField(max_length=300)
    option_c = models.CharField(max_length=300)
    option_d = models.CharField(max_length=300, blank=True)
    correct = models.CharField(max_length=1)  # 'A'..'D'
    explanation = models.TextField()          # giai thich tieng Viet
    level = models.CharField(max_length=5, default='B1')

    def options(self):
        opts = [('A', self.option_a), ('B', self.option_b), ('C', self.option_c)]
        if self.option_d:
            opts.append(('D', self.option_d))
        return opts

    def correct_text(self):
        return dict(self.options()).get(self.correct, '')

    def __str__(self):
        return self.text[:60]


class WritingLesson(models.Model):
    title = models.CharField(max_length=200)
    title_vi = models.CharField(max_length=200)
    task_no = models.PositiveIntegerField(default=1)  # VSTEP Writing Task 1 / 2
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class SpeakingLesson(models.Model):
    part = models.PositiveIntegerField(default=1)  # VSTEP Speaking Part 1-3
    title = models.CharField(max_length=200)
    title_vi = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class QuizAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attempts')
    kind = models.CharField(max_length=20)     # grammar / vocab / reading / listening / mock
    label = models.CharField(max_length=200)   # ten bai (Unit 3, Topic Food...)
    score = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    @property
    def percent(self):
        return round(self.score * 100 / self.total) if self.total else 0

    def __str__(self):
        return f'{self.user} - {self.label}: {self.score}/{self.total}'


class WordProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='word_progress')
    word = models.ForeignKey(VocabWord, on_delete=models.CASCADE)
    known = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'word')
