from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    Episode = models.CharField(max_length=200)
    chapter = models.TextField()
    Publicationdate = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title
