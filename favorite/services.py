from django.db import transaction

from favorite.models import Favorite



def is_favorite(*, user, news):
    return Favorite.objects.filter(user=user, news=news).exists()


@transaction.atomic
def add_favorite(*, user, news):
    favorite, _ = Favorite.objects.get_or_create(user=user, news=news)
    return favorite



def remove_favorite(*, user, news):
    deleted_count, _ = Favorite.objects.filter(user=user, news=news).delete()
    return deleted_count > 0



def list_favorites(*, user, page=1, page_size=10):
    offset = (page - 1) * page_size
    queryset = Favorite.objects.filter(user=user).select_related("news").order_by("-created_at", "-id")
    favorites = list(queryset[offset:offset + page_size])
    total = queryset.count()
    return favorites, total



def clear_favorites(*, user):
    deleted_count, _ = Favorite.objects.filter(user=user).delete()
    return deleted_count
