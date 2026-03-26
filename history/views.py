from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from news.services import get_news_detail
from utils.authentication import BearerTokenAuthentication
from utils.response import success_response

from .assemblers import (
    build_history_clear_response,
    build_history_list_response,
    build_history_record,
)
from .serializers import HistoryAddSerializer, HistoryListQuerySerializer
from .services import add_history, clear_history, delete_history, list_histories


class HistoryAddAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def post(self, request):
        serializer = HistoryAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        news_id = serializer.validated_data["news_id"]
        news = get_news_detail(news_id=news_id)
        if news is None:
            raise NotFound("not found")

        history = add_history(user=request.user, news=news)
        return success_response(data=build_history_record(history=history))


class HistoryListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def get(self, request):
        query_serializer = HistoryListQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)

        page = query_serializer.validated_data["page"]
        page_size = query_serializer.validated_data["page_size"]
        histories, total = list_histories(user=request.user, page=page, page_size=page_size)

        return success_response(
            data=build_history_list_response(
                histories=histories,
                total=total,
                page=page,
                page_size=page_size,
            )
        )


class HistoryDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def delete(self, request, history_id):
        deleted = delete_history(user=request.user, history_id=history_id)
        if not deleted:
            raise NotFound("not found")
        return success_response()


class HistoryClearAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def delete(self, request):
        deleted_count = clear_history(user=request.user)
        return success_response(data=build_history_clear_response(deleted_count=deleted_count))
