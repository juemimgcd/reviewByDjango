from .serializers import FavoriteNewsItemSerializer


def build_favorite_check_response(*, is_favorite: bool):
    """组装“是否已收藏”接口的响应数据。"""

    return {
        "is_favorite":is_favorite
    }



def build_favorite_record(*, favorite):
    """组装“新增收藏”接口返回的单条收藏记录数据。"""

    return {
        "favoriteId":favorite.id,
        "userId":favorite.user_id,
        "newsId":favorite.news_id,
        "created_at":favorite.created_at
    }



def build_favorite_list_response(*, favorites, total: int, page: int, page_size: int):
    """组装“收藏列表”接口的响应数据。"""

    list = FavoriteNewsItemSerializer(favorites,many=True).data
    has_more = (page - 1)*page_size < total

    return {
        "list":list,
        "total":total,
        "hasMore":has_more
    }



def build_favorite_clear_response(*, deleted_count: int):
    """组装“清空收藏”接口的响应数据。"""

    return {
        "deletedCount":deleted_count
    }


