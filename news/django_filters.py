from django_filters import FilterSet
from .models import NewsArticle


class NewsFilter(FilterSet):
    class Search:
        model = NewsArticle
        cat = (
            "date",
            "time",
        )
