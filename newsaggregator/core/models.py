from django.db import models

from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=300)
    summary = models.TextField(blank=True)
    url = models.URLField()
    source = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="General")
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source} - {self.title}"
