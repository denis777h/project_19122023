from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


# Create your models here.

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    deskripts = models.TextField()
    quentiny = models.IntegerField(
        validators=[MinValueValidator(0)],
    )


    def __str__(self):
        return self.title



    def get_absolude_urls(self, reverse=None):
        return reverse('default', args=[str(self.search)])

    def get_absolute_url(self):
        return reverse('default', args=[str(self.id)])


    def __add__(self):
        return self.get_absolute_url()
    def __str__(self):
        return self.deskripts
    def __str__(self):
        return self.get_absolude_urls()




