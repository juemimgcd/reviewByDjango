from rest_framework import serializers

from history.models import History


class HistoryAddSerializer(serializers.Serializer):
    """
    新增浏览历史接口的请求体。

    需要字段：
    - newsId: int，新闻主键 ID。
    """
    newsId = serializers.IntegerField(source="news.news_id",min_value=1)



class HistoryRecordSerializer(serializers.Serializer):
    """
    浏览历史记录基础信息。

    需要字段：
    - id: int，历史记录 ID。
    - userId: int，用户 ID。
    - newsId: int，新闻 ID。
    - viewTime: datetime，最近浏览时间。
    """
    id = serializers.IntegerField(source="history_id",min_value=1)
    userId = serializers.IntegerField(source="users.user_id",min_value=1)
    newsId = serializers.IntegerField(source="news.news_id",min_value=1)
    viewTime = serializers.DateTimeField()




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
    """
    浏览历史列表接口的查询参数。

    需要字段：
    - page: int，页码，从 1 开始。
    - pageSize: int，每页数量。
    """
    page = serializers.IntegerField(min_value=1)
    pageSize = serializers.IntegerField(source="page_size",required=False,min_value=1,max_value=100)



class HistoryListResponseSerializer(serializers.Serializer):
    """
    浏览历史列表接口的响应数据。

    需要字段：
    - list: list[HistoryNewsItemSerializer]，历史记录列表数据。
    - total: int，历史记录总数。
    - hasMore: bool，是否还有下一页。
    """
    list = HistoryNewsItemSerializer(many=True)
    total = serializers.IntegerField()
    hasMore = serializers.BooleanField()










