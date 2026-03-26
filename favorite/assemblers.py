from .serializers import FavoriteNewsItemSerializer


def build_favorite_check_response(*, is_favorite: bool):
    return {
        "isFavorite": is_favorite,
    }


def build_favorite_record(*, favorite):
    return {
        "id": favorite.id,
        "userId": favorite.user_id,
        "newsId": favorite.news_id,
        "createdAt": favorite.created_at,
    }


def build_favorite_list_response(*, favorites, total: int, page: int, page_size: int):
    return {
        "list": FavoriteNewsItemSerializer(favorites, many=True).data,
        "total": total,
        "hasMore": page * page_size < total,
    }


def build_favorite_clear_response(*, deleted_count: int):
    return {
        "deletedCount": deleted_count,
    }
