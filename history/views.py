from rest_framework.views import APIView
from utils.response import success_response
from rest_framework.permissions import IsAuthenticated
from utils.authentication import BearerTokenAuthentication
from .models import History
from .services import (
    add_history,
    list_histories,
    delete_history,
    clear_history
)
from news.services import get_news_detail
from .serializers import (
    HistoryAddSerializer,
    HistoryRecordSerializer,
    HistoryNewsItemSerializer,
    HistoryListResponseSerializer,
    HistoryListQuerySerializer
)






class HistoryAddAPIView(APIView):
    """
    处理新增浏览历史接口。

    需要完成的功能：
    - 接收当前登录用户和请求体 `newsId:int`。
    - 校验新闻是否存在。
    - 调用历史记录逻辑，完成新增或更新时间。
    - 返回历史记录基础信息。
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def post(self,request):
        serializer = HistoryAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        news_id = serializer.validated_data["news_id"]
        news = get_news_detail(news_id=news_id)

        history = add_history(user=request.user,news=news)

        resp_data = {
            "id":history.pk,
            "userId":request.user.pk,
            "newsId":news.pk,
            "viewTime":history.view_time
        }
        resp_serializer = HistoryRecordSerializer(data=resp_data)

        return success_response(data=resp_serializer.data)



class HistoryListAPIView(APIView):
    """
    处理浏览历史列表接口。

    需要完成的功能：
    - 接收当前登录用户以及分页参数 `page:int`、`pageSize:int`。
    - 分页查询历史记录，并关联新闻详情字段。
    - 计算 `total` 和 `hasMore`。
    - 返回历史记录分页数据。
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]

    def get(self,request):
        queryset_serializer = HistoryListQuerySerializer(data=request.params)
        queryset_serializer.is_valid(raise_exception=True)

        page = queryset_serializer.validated_data["page"]
        page_size = queryset_serializer.validated_data["pageSize"]

        histories,total = list_histories(user=request.user,page=page,page_size=page_size)
        items_serializer = HistoryNewsItemSerializer(data=histories, many=True)

        has_more = page * page_size < total
        resp_data = {
            "list":items_serializer.data,
            "total":total,
            "hasMore":has_more
        }

        resp_serializer = HistoryListResponseSerializer(data=resp_data)

        return success_response(data=resp_serializer.data)










class HistoryDeleteAPIView(APIView):
    """
    处理删除单条浏览历史接口。

    需要完成的功能：
    - 接收当前登录用户和路径参数 `history_id:int`。
    - 删除属于当前用户的指定历史记录。
    - 当历史记录不存在时返回 404。
    - 删除成功后返回统一成功响应。
    """


class HistoryClearAPIView(APIView):
    """
    处理清空浏览历史接口。

    需要完成的功能：
    - 接收当前登录用户。
    - 删除该用户全部历史记录。
    - 返回清空成功的统一响应。
    """
