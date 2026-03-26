from rest_framework import serializers


class FavoriteCheckQuerySerializer(serializers.Serializer):
    """
    收藏检查接口的查询参数。

    需要字段：
    - newsId: int，新闻主键 ID。
    """


class FavoriteRemoveQuerySerializer(serializers.Serializer):
    """
    取消收藏接口的查询参数。

    需要字段：
    - newsId: int，新闻主键 ID。
    """


class FavoriteAddSerializer(serializers.Serializer):
    """
    添加收藏接口的请求体。

    需要字段：
    - newsId: int，新闻主键 ID。
    """


class FavoriteCheckResponseSerializer(serializers.Serializer):
    """
    收藏检查接口的响应数据。

    需要字段：
    - isFavorite: bool，当前用户是否已收藏该新闻。
    """


class FavoriteRecordSerializer(serializers.Serializer):
    """
    收藏记录基础信息。

    需要字段：
    - id: int，收藏记录 ID。
    - userId: int，用户 ID。
    - newsId: int，新闻 ID。
    - createdAt: datetime，收藏创建时间。
    """


class FavoriteNewsItemSerializer(serializers.Serializer):
    """
    收藏列表中的新闻项数据。

    需要字段：
    - id: int，新闻 ID。
    - title: str，新闻标题。
    - description: str | None，新闻简介。
    - image: str | None，新闻封面图片地址。
    - author: str | None，新闻作者。
    - categoryId: int，新闻分类 ID。
    - views: int，新闻浏览量。
    - publishTime: datetime，新闻发布时间。
    - favoriteId: int，收藏记录 ID。
    - favoriteTime: datetime，收藏时间。
    """


class FavoriteListQuerySerializer(serializers.Serializer):
    """
    收藏列表接口的查询参数。

    需要字段：
    - page: int，页码，从 1 开始。
    - pageSize: int，每页数量。
    """


class FavoriteListResponseSerializer(serializers.Serializer):
    """
    收藏列表接口的响应数据。

    需要字段：
    - list: list[FavoriteNewsItemSerializer]，收藏列表数据。
    - total: int，收藏总数。
    - hasMore: bool，是否还有下一页。
    """
