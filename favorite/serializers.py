from rest_framework import serializers

from favorite.models import Favorite


class FavoriteCheckQuerySerializer(serializers.Serializer):
    """定义“检查是否收藏”接口需要的查询参数字段。"""
    newsId = serializers.IntegerField(source="news_id")
    pass


class FavoriteRemoveQuerySerializer(FavoriteCheckQuerySerializer):
    """定义“取消收藏”接口需要的查询参数字段。"""

    pass


class FavoriteAddSerializer(FavoriteCheckQuerySerializer):
    """定义“添加收藏”接口需要的请求体字段。"""
    pass


class FavoriteNewsItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="news_id")
    title = serializers.CharField(source="news.title")
    description = serializers.CharField(source="news.description", allow_null=True, required=False)
    image = serializers.CharField(source="news.image", allow_null=True, required=False)
    author = serializers.CharField(source="news.author", allow_null=True, required=False)
    categoryId = serializers.IntegerField(source="news.category_id")
    views = serializers.IntegerField(source="news.views")
    publishTime = serializers.DateTimeField(source="news.publish_time")
    favoriteId = serializers.IntegerField(source="id")
    favoriteTime = serializers.DateTimeField(source="created_at")

    class Meta:
        model = Favorite
        fields = [
            "id",
            "title",
            "description",
            "image",
            "author",
            "categoryId",
            "views",
            "publishTime",
            "favoriteId",
            "favoriteTime",
        ]


class FavoriteListQuerySerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    pageSize = serializers.IntegerField(
        source="page_size",
        required=False,
        min_value=1,
        max_value=100,
        default=10,
    )
