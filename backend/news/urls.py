from django.urls import path
import news.views as view


urlpatterns = [
    path('',view.TopNewsView.as_view()),
    path('<int:pk>',view.EditNews.as_view()),
]
