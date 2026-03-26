from .serializers import HistoryNewsItemSerializer


def build_history_record(*, history):
    return {
        "id":history.id,
        "userId":history.user_id,
        "newsId":history.news_id,
        "view_time":history.view_time
    }




def build_history_list_response(*, histories, total: int, page: int, page_size: int):

    has_more = total > page * page_size
    h_list = HistoryNewsItemSerializer(histories,many=True).data

    return {
        "list":h_list,
        "total":total,
        "hasMore":has_more
    }



    raise NotImplementedError("请在这里实现 build_history_list_response")


def build_history_clear_response(*, deleted_count: int):
    return {
        "deletedCount":deleted_count
    }
