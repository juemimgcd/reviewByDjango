from rest_framework import serializers
from .models import News,Category


class CategoryQuerySerializer(serializers.Serializer):
    skip = serializers.IntegerField(required=False,min_value=0,default=0)
    limit = serializers.IntegerField(required=False,min_value=1,max_value=20,default=20)



class CategoryResponseSerializer(serializers.ModelSerializer):
    sortOrder = serializers.IntegerField(source="sort_order")

    class Meta:
        model = Category
        fields = ["id", "name", "sortOrder"]



class NewsBaseSerializer(serializers.ModelSerializer):
    categoryId = serializers.IntegerField(source="category_id")
    publishTime = serializers.DateTimeField(source="publish_time")

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "description",
            "image",
            "author",
            "categoryId",
            "views",
            "publishTime",
        ]


class NewsListQuerySerializer(serializers.Serializer):
    categoryId = serializers.IntegerField(source="category_id", min_value=1)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    pageSize = serializers.IntegerField(source="page_size", required=False, min_value=1, max_value=100, default=10)



class NewsListResponseSerializer(serializers.Serializer):
    list = NewsBaseSerializer(many=True)
    total = serializers.IntegerField()



class NewsDetailQuerySerializer(serializers.Serializer):
    id = serializers.IntegerField(source="news_id", min_value=1)


class NewsDetailResponseSerializer(NewsBaseSerializer):
    pass


class RelatedNewsSerializer(NewsBaseSerializer):
    pass

