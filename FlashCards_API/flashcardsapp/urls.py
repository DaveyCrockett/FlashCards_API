from django.urls import path
from . import views


urlpatterns = [
    path('flashcardsapp/', views.FlashCardList.as_view()),
]