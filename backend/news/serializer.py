from rest_framework import serializers
from news.models import TopArticle


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=TopArticle
        fields = '__all__'



