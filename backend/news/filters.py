import django_filters
from news.models import TopArticle

class TopArticalFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(lookup_expr='icontains', field_name='description',label='Search by Query')

    class Meta:
        model = TopArticle
        fields = ['q'] 