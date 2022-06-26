from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=400)