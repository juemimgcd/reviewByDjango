from rest_framework.views import APIView


class FavoriteCheckAPIView(APIView):
    """
    处理收藏检查接口。

    需要完成的功能：
    - 接收当前登录用户和查询参数 `newsId:int`。
    - 校验当前请求的认证状态。
    - 调用收藏查询逻辑判断是否已收藏。
    - 返回 `isFavorite: bool` 的统一响应结构。
    """


class FavoriteAddAPIView(APIView):
    """
    处理添加收藏接口。

    需要完成的功能：
    - 接收当前登录用户和请求体 `newsId:int`。
    - 校验新闻是否存在。
    - 调用收藏新增逻辑，重复收藏时保持幂等。
    - 返回收藏记录基础信息。
    """


class FavoriteRemoveAPIView(APIView):
    """
    处理取消收藏接口。

    需要完成的功能：
    - 接收当前登录用户和查询参数 `newsId:int`。
    - 删除当前用户对应新闻的收藏记录。
    - 当收藏记录不存在时返回 404。
    - 删除成功后返回统一成功响应。
    """


class FavoriteListAPIView(APIView):
    """
    处理收藏列表接口。

    需要完成的功能：
    - 接收当前登录用户以及分页参数 `page:int`、`pageSize:int`。
    - 分页查询用户收藏列表，并关联新闻详情字段。
    - 计算 `total` 和 `hasMore`。
    - 返回收藏列表分页数据。
    """


class FavoriteClearAPIView(APIView):
    """
    处理清空收藏接口。

    需要完成的功能：
    - 接收当前登录用户。
    - 删除该用户全部收藏记录。
    - 返回清空结果和删除数量相关提示信息。
    """
