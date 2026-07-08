from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import (ListeningTrack, ReadingPassage, Unit, VocabTopic)


class StaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0
    protocol = 'https'

    def items(self):
        return ['home', 'grammar_list', 'vocab_topics', 'reading_list',
                'listening_list', 'writing', 'speaking', 'mock_test_start']

    def location(self, item):
        return reverse(item)


class UnitSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Unit.objects.all()

    def location(self, obj):
        return reverse('grammar_detail', args=[obj.pk])


class VocabTopicSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return VocabTopic.objects.all()

    def location(self, obj):
        return reverse('vocab_detail', args=[obj.pk])


class ReadingSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    protocol = 'https'

    def items(self):
        return ReadingPassage.objects.all()

    def location(self, obj):
        return reverse('reading_detail', args=[obj.pk])


class ListeningSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    protocol = 'https'

    def items(self):
        return ListeningTrack.objects.all()

    def location(self, obj):
        return reverse('listening_detail', args=[obj.pk])
