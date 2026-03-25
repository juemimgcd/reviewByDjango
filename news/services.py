from django.db.models import F
from .models import Category, News


def list_categories(skip: int = 0, limit: int = 20):
    if limit <= 0:
        return []
    return list(Category.objects.all().order_by("sort_order", "id")[skip:skip + limit])


def list_news(category_id: int, skip: int = 0, limit: int = 20):
    if limit <= 0:
        return []

    return list(
        News.objects.filter(category_id=category_id)
        .order_by("-publish_time", "-id")[skip:skip + limit]
    )


def get_news_total(category_id:int):
    return News.objects.filter(category_id=category_id).count()


def get_news_detail(*, news_id: int):
    return News.objects.filter(id=news_id).first()


def increase_news_views(*, news_id: int):
    return News.objects.filter(id=news_id).update(views=F("views") + 1)


def get_related_news(*, category_id: int, news_id: int, limit: int = 5):
    return list(
        News.objects.filter(category_id=category_id)
        .exclude(id=news_id)
        .order_by("-views", "-publish_time")[:limit]
    )


