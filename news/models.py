from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Search(models.Model):
    keyword = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.keyword

class Article(models.Model):
    search = models.ForeignKey(Search, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    url = models.URLField()
    published_at = models.DateTimeField()
    source_name = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
