from .models import History
from news.models import News
from users.models import User
from django.db.models import F
from datetime import datetime


def add_history(*, user, news):
    """
    新增或更新当前用户的浏览历史记录。
    需要完成的功能：
    - 接收用户和新闻对象。
    - 如果该用户已经浏览过这条新闻，则更新最近浏览时间。
    - 如果没有浏览过，则创建新的历史记录。
    - 返回最新的历史记录对象。
    """
    history = History.objects.filter(user=user, news=news)
    if history:
        history.view_time = datetime.now()
        history.save()

    else:
        history = History.objects.create(
            user=user,
            news=news,
            view_time=datetime.now()
        )
        return history




def list_histories(*, user, page=1, page_size=10):
    """
    分页获取当前用户的浏览历史列表。

    需要完成的功能：
    - 接收用户、页码和分页大小。
    - 按最近浏览时间倒序查询历史记录。
    - 关联新闻信息并组装列表数据。
    - 返回当前页数据和历史总数。
    """
    offset = (page - 1)*page_size
    histories = list(History.objects.filter(user=user).all()[offset:offset+page_size])
    total = History.objects.filter(user=user).count()

    return histories,total





def delete_history(*, user, history_id):
    """
    删除当前用户的一条浏览历史记录。

    需要完成的功能：
    - 接收用户和历史记录 ID。
    - 仅删除属于当前用户的指定历史记录。
    - 返回是否删除成功。
    """
    history = History.objects.filter(user=user,history_id=history_id)
    history.delete()






def clear_history(*, user):
    """
    清空当前用户的全部浏览历史。

    需要完成的功能：
    - 接收当前用户。
    - 删除该用户全部历史记录。
    - 返回被删除的记录数量。
    """
    histories = History.objects.filter(user=user)
    histories.delete()












