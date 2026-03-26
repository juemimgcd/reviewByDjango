from rest_framework import serializers

from history.models import History


class HistoryAddSerializer(serializers.Serializer):
    newsId = serializers.IntegerField(source="news_id", min_value=1)


class HistoryNewsItemSerializer(serializers.ModelSerializer):
    """
    浏览历史列表中的新闻项数据。

    需要字段：
    - id: int，新闻 ID。
    - title: str，新闻标题。
    - description: str | None，新闻简介。
    - image: str | None，新闻封面图片地址。
    - author: str | None，新闻作者。
    - categoryId: int，新闻分类 ID。
    - views: int，新闻浏览量。
    - publishTime: datetime，新闻发布时间。
    - historyId: int，历史记录 ID。
    - viewTime: datetime，最近浏览时间。
    """
    id = serializers.IntegerField(source="news.news_id")
    title = serializers.CharField(source="news.title")
    description = serializers.CharField(source="news.description", allow_null=True, required=False)
    image = serializers.CharField(source="news.image", allow_null=True, required=False)
    author = serializers.CharField(source="news.author", allow_null=True, required=False)
    categoryId = serializers.IntegerField(source="news.category_id")
    views = serializers.IntegerField(source="news.views")
    publishTime = serializers.DateTimeField(source="news.publish_time")
    historyId = serializers.IntegerField(source="history_id")
    viewTime = serializers.DateTimeField(source="view_time")

    class Meta:
        model = History
        fields = [
            "id",
            "title",
            "description",
            "image",
            "author",
            "categoryId",
            "views",
            "publishTime",
            "historyId",
            "viewTime",
        ]





class HistoryListQuerySerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    pageSize = serializers.IntegerField(
        source="page_size",
        required=False,
        min_value=1,
        max_value=100,
        default=10,
    )










