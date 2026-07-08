from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Auth
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='learning/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Grammar
    path('grammar/', views.grammar_list, name='grammar_list'),
    path('grammar/<int:pk>/', views.grammar_detail, name='grammar_detail'),
    path('grammar/<int:pk>/quiz/', views.grammar_quiz, name='grammar_quiz'),

    # Vocabulary
    path('vocab/', views.vocab_topics, name='vocab_topics'),
    path('vocab/<int:pk>/', views.vocab_detail, name='vocab_detail'),
    path('vocab/<int:pk>/flashcards/', views.flashcards, name='flashcards'),
    path('vocab/<int:pk>/quiz/', views.vocab_quiz, name='vocab_quiz'),
    path('vocab/word/<int:pk>/mark/', views.mark_word, name='mark_word'),

    # Reading
    path('reading/', views.reading_list, name='reading_list'),
    path('reading/<int:pk>/', views.reading_detail, name='reading_detail'),

    # Listening
    path('listening/', views.listening_list, name='listening_list'),
    path('listening/<int:pk>/', views.listening_detail, name='listening_detail'),

    # Writing & Speaking
    path('writing/', views.writing, name='writing'),
    path('speaking/', views.speaking, name='speaking'),

    # Mock test
    path('mock-test/', views.mock_test_start, name='mock_test_start'),
    path('mock-test/run/', views.mock_test, name='mock_test'),

    # Progress
    path('progress/', views.progress, name='progress'),
]
