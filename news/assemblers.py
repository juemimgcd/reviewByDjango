from .serializers import CategoryResponseSerializer, NewsBaseSerializer


def build_category_list_response(categories):
    return CategoryResponseSerializer(categories, many=True).data


def build_news_list_response(*, news_items, total: int):
    return {
        "list": NewsBaseSerializer(news_items, many=True).data,
        "total": total,
    }


def build_news_detail_response(*, detail, related):
    return {
        "detail": NewsBaseSerializer(detail).data,
        "related": NewsBaseSerializer(related, many=True).data,
    }
