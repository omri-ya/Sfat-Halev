from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def create(self, validated_data):
        return Article.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)