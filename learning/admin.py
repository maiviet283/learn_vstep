from django.contrib import admin

from .models import (GrammarLesson, ListeningTrack, Question, QuizAttempt,
                     ReadingPassage, SpeakingLesson, Unit, VocabTopic,
                     VocabWord, WordProgress, WritingLesson)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'title_vi', 'level')


@admin.register(VocabWord)
class VocabWordAdmin(admin.ModelAdmin):
    list_display = ('word', 'pos', 'meaning_vi', 'topic', 'level')
    list_filter = ('topic', 'level')
    search_fields = ('word', 'meaning_vi')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'skill', 'unit', 'topic', 'correct', 'level')
    list_filter = ('skill', 'level', 'unit', 'topic')
    search_fields = ('text',)


admin.site.register([GrammarLesson, VocabTopic, ReadingPassage, ListeningTrack,
                     WritingLesson, SpeakingLesson, QuizAttempt, WordProgress])
