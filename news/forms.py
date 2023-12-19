from django import forms
from django.core.exceptions import ValidationError

from .models import NewsArticle


class NewsArticleForm(forms.ModelForm):
    deskripts = forms.CharField(min_length=20)
    class Meta:
        model = NewsArticle
        search = [
            'name',
            'data',
            'autors',
        ]
        pass
        def clean(self):
            cleaners = super().clean()
            name = cleaners.get("name")
            deskripts = cleaners.get("destripts")

            if name == deskripts:
                raise ValidationError(
                    "Описание должно быть идентичным"
                )
            return cleaners


