# built in
from django.shortcuts import render
from rest_framework import generics,pagination
from rest_framework.permissions import IsAuthenticated , IsAdminUser

# user deefineed
from news.serializer import NewsSerializer
from news.models import TopArticle



class TopNewsView(generics.ListAPIView):
    serializer_class=NewsSerializer
    permission_classes=[IsAuthenticated]
    queryset = TopArticle.objects.all()


class EditNews(generics.ListCreateAPIView):
    serializer_class=NewsSerializer
    permission_classes=[IsAdminUser]
    queryset = TopArticle.objects.all()
    lookup_field='pk'