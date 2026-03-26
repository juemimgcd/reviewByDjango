from django.db import transaction
from django.utils import timezone
from django.db.models import F
from .models import History


@transaction.atomic
def add_history(*, user, news):
    history,created = History.objects.get_or_create(
        user=user,
        news=news,
        defaults={"view_time":timezone.now()}
    )

    if not created:
        history.view_time = timezone.now()
        history.save(update_fields=["view_time"])
    
    return history


def list_histories(*, user, page=1, page_size=10):
    offset = (page - 1)*page_size
    queryset = History.objects.filter(user=user).select_related("news").order_by("-view_time")
    histories,total = list(queryset[offset:offset+page_size]),queryset.count()
    return histories,total


def delete_history(*, user, history_id):

    deleted,_ = History.objects.filter(user=user,id=history_id).delete()
    return deleted > 0



def clear_history(*, user):

    deleted,_ = History.objects.filter(user=user).delete()
    return deleted > 0


