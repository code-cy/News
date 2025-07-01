# built in
from django.shortcuts import render
from rest_framework import generics,pagination
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
# user deefineed
from news.serializer import NewsSerializer
from news.models import TopArticle
from .tasks import save_articles
from news.filters import TopArticalFilter
from .pagination import TopArticalPagination


class TopNewsView(generics.ListAPIView):
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class=TopArticalFilter
    pagination_class=TopArticalPagination

    def get_queryset(self):
        query =self.request.query_params.dict()  # getting the query paara and passing them to save_artical

        print(query)
        save_articles(query)
        if TopArticle.objects.count() > 20:
            TopArticle.objects.exclude(
                id__in=TopArticle.objects.order_by('-id')[:20].values_list('id', flat=True)
            ).delete()                                                                              #deleteing the artical when it more then 20. only top 20 articals while be save
        


        return TopArticle.objects.all()




class EditNews(generics.ListCreateAPIView):
    serializer_class=NewsSerializer
    permission_classes=[IsAdminUser]
    queryset = TopArticle.objects.all()
    lookup_field='pk'

def create_news(request):
    save_articles()
    return HttpResponse("YOU NEWS CREATED SUCCESFULLY")