# built in
from django.shortcuts import render
from rest_framework import generics,pagination
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.http import HttpResponse

# user deefineed
from news.serializer import NewsSerializer
from news.models import TopArticle
from .tasks import save_articles


class TopNewsView(generics.ListAPIView):
    serializer_class=NewsSerializer
    # permission_classes=[IsAuthenticated,IsAdminUser]
    def get_queryset(self):
        if not TopArticle.objects.exists():
            save_articles()
        return TopArticle.objects.all()


class EditNews(generics.ListCreateAPIView):
    serializer_class=NewsSerializer
    permission_classes=[IsAdminUser]
    queryset = TopArticle.objects.all()
    lookup_field='pk'

def create_news(request):
    save_articles()
    return HttpResponse("YOU NEWS CREATED SUCCESFULLY")