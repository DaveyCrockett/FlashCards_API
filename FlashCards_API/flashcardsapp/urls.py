from django.urls import path
from . import views

urlpatterns = [
    path('flashcardsapp/', views.FlashCardList.as_view()),
    path('flashcardsapp/<int:collection_id>', views.FlashCardDetail.as_view()),
    path('flashcardsapp/<int:collection_id>/<int:id>', views.FlashCardDetail2.as_view()),
]
