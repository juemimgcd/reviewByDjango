from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from news.services import get_news_detail
from utils.authentication import BearerTokenAuthentication
from utils.response import success_response

from .assemblers import (
    build_favorite_check_response,
    build_favorite_clear_response,
    build_favorite_list_response,
    build_favorite_record,
)
from .serializers import (
    FavoriteAddSerializer,
    FavoriteCheckQuerySerializer,
    FavoriteListQuerySerializer,
    FavoriteRemoveQuerySerializer,
)
from .services import add_favorite, clear_favorites, is_favorite, list_favorites, remove_favorite


class FavoriteCheckAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def get(self, request):
        serializer = FavoriteCheckQuerySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        news_id = serializer.validated_data["news_id"]
        news = get_news_detail(news_id=news_id)
        if news is None:
            raise NotFound("not found")

        return success_response(
            data=build_favorite_check_response(is_favorite=is_favorite(user=request.user, news=news))
        )


class FavoriteAddAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def post(self, request):
        serializer = FavoriteAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        news_id = serializer.validated_data["news_id"]
        news = get_news_detail(news_id=news_id)
        if news is None:
            raise NotFound("not found")

        favorite = add_favorite(user=request.user, news=news)
        return success_response(data=build_favorite_record(favorite=favorite))


class FavoriteRemoveAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def delete(self, request):
        serializer = FavoriteRemoveQuerySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        news_id = serializer.validated_data["news_id"]
        news = get_news_detail(news_id=news_id)
        if news is None:
            raise NotFound("not found")

        deleted = remove_favorite(user=request.user, news=news)
        if not deleted:
            raise NotFound("not found")

        return success_response()


class FavoriteListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def get(self, request):
        serializer = FavoriteListQuerySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        page = serializer.validated_data["page"]
        page_size = serializer.validated_data["page_size"]
        favorites, total = list_favorites(user=request.user, page=page, page_size=page_size)

        return success_response(
            data=build_favorite_list_response(
                favorites=favorites,
                total=total,
                page=page,
                page_size=page_size,
            )
        )


class FavoriteClearAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def delete(self, request):
        deleted_count = clear_favorites(user=request.user)
        return success_response(data=build_favorite_clear_response(deleted_count=deleted_count))
