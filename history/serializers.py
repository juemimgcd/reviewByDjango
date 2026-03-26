from rest_framework import serializers

from history.models import History


class HistoryAddSerializer(serializers.Serializer):
    newsId = serializers.IntegerField(source="news_id",min_value=1)



class HistoryNewsItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="news_id",min_value=1,max_value=9999)
    title= serializers.CharField(source="news.title")
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

    page = serializers.IntegerField(min_value=1,max_value=1000,default=1)
    pageSize = serializers.IntegerField(source="page_size",required=False,min_value=1,max_value=20,default=10)


