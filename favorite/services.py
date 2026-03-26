from django.db import transaction

from favorite.models import Favorite


def is_favorite(*, user, news):
    return Favorite.objects.filter(user=user, news=news).exists()



@transaction.atomic
def add_favorite(*, user, news):
    """新增收藏；如果记录已存在，直接返回现有收藏记录。"""
    favorite,created = Favorite.objects.get_or_create(
        user=user,
        news=news,
    )

    return favorite



def remove_favorite(*, user, news):
    """取消当前用户对指定新闻的收藏，并返回是否删除成功。"""
    deleted_count,_ = Favorite.objects.filter(user=user,news=news).delete()

    return deleted_count > 0




def list_favorites(*, user, page=1, page_size=10):
    """按分页获取当前用户的收藏列表和总数。"""

    offset = (page - 1)*page_size
    queryset = Favorite.objects.filter(user=user).select_related("news").order_by("-created_at", "-id")

    favorites = list(queryset[offset:offset+page_size])
    total = queryset.count()

    return favorites,total


def clear_favorites(*, user):
    """清空当前用户的全部收藏，并返回删除数量。"""

    deleted_count,_ = Favorite.objects.filter(user=user).delete()
    return deleted_count

