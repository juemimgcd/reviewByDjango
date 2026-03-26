from .serializers import HistoryNewsItemSerializer


def build_history_record(*, history):
    return {
        "id": history.id,
        "userId": history.user_id,
        "newsId": history.news_id,
        "viewTime": history.view_time,
    }


def build_history_list_response(*, histories, total: int, page: int, page_size: int):
    return {
        "list": HistoryNewsItemSerializer(histories, many=True).data,
        "total": total,
        "hasMore": page * page_size < total,
    }


def build_history_clear_response(*, deleted_count: int):
    return {
        "deletedCount": deleted_count,
    }
