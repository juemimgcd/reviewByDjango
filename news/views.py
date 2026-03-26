from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from utils.response import success_response

from .serializers import (
    CategoryQuerySerializer,
    CategoryResponseSerializer,
    NewsDetailQuerySerializer,
    NewsDetailResponseSerializer,
    NewsListQuerySerializer,
    NewsListResponseSerializer,
    RelatedNewsSerializer,
)
from .services import (
    get_news_detail,
    get_news_total,
    get_related_news,
    increase_news_views,
    list_categories,
    list_news,
)


# Create your views here.


class CategoryAPIView(APIView):
    def get(self, request):
        query_serializer = CategoryQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)

        categories = list_categories(**query_serializer.validated_data)
        serializer = CategoryResponseSerializer(categories, many=True)
        return success_response(data=serializer.data)


class NewsListAPIView(APIView):
    def get(self, request):
        query_serializer = NewsListQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)

        category_id = query_serializer.validated_data["category_id"]
        page = query_serializer.validated_data["page"]
        page_size = query_serializer.validated_data["page_size"]
        offset = (page - 1) * page_size

        news_items = list_news(category_id=category_id, skip=offset, limit=page_size)
        total = get_news_total(category_id=category_id)

        resp_serializer = NewsListResponseSerializer({"list": news_items, "total": total or 0})

        resp_data = resp_serializer.data
        return success_response(data=resp_data)



class NewsDetailAPIView(APIView):
    def get(self, request):
        query_serializer = NewsDetailQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)

        news_id = query_serializer.validated_data["news_id"]
        detail = get_news_detail(news_id=news_id)
        if detail is None:
            raise NotFound("not found")

        increase_news_views(news_id=news_id)
        detail.refresh_from_db()
        related = get_related_news(category_id=detail.category_id, news_id=detail.id)

        return success_response(
            data={
                "detail": NewsDetailResponseSerializer(detail).data,
                "related": RelatedNewsSerializer(related, many=True).data,
            }
        )









