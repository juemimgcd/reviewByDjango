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
        """实现“检查是否收藏”的参数校验、新闻查询、状态判断和响应返回。"""
        query_serializer = FavoriteCheckQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)

        news_id = query_serializer.validated_data["news_id"]
        news = get_news_detail(news_id=news_id)
        if news is None:
            raise NotFound("not found")
        favorite = is_favorite(user=request.user,news=news)
        
        

        return success_response(data=build_favorite_check_response(is_favorite=favorite))




class FavoriteAddAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def post(self, request):
        """实现“添加收藏”的参数校验、新闻查询、收藏保存和响应返回。"""

        serializer = FavoriteAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        news_id = serializer.validated_data["news_id"]
        news = get_news_detail(news_id=news_id)
        if news is None:
            raise NotFound("not found")
        favorite = add_favorite(user=request.user,news=news)
        
        

        return success_response(data=build_favorite_record(favorite=favorite))





class FavoriteRemoveAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def delete(self, request):
        """实现“取消收藏”的参数校验、新闻查询、删除操作和响应返回。"""
        query_serializer = FavoriteRemoveQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)
        

        news_id = query_serializer.validated_data["news_id"]
        news = get_news_detail(news_id=news_id)
        if news is None:
            raise NotFound("not found")
        deleted_count = remove_favorite(user=request.user,news=news)

        return success_response()



class FavoriteListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def get(self, request):
        """实现“收藏列表”的分页参数校验、数据查询和响应返回。"""
        query_serializer = FavoriteListQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)
        
        page = query_serializer.validated_data["page"]
        page_size = query_serializer.validated_data["page_size"]

        favorite_list,total = list_favorites(user=request.user)

        return success_response(
            data=build_favorite_list_response(favorites=favorite_list,page=page,page_size=page_size,total=total)
                                )


class FavoriteClearAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def delete(self, request):
        """实现“清空收藏”的删除操作和响应返回。"""
        query_serializer = FavoriteRemoveQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)

        deleted_count = clear_favorites(user=request.user)

        return success_response(data=build_favorite_clear_response(deleted_count=deleted_count))

