import uuid
from datetime import timedelta
from django.db import transaction
from django.utils import timezone

from .models import User, UserLoginLog, UserToken


def get_user_by_name(username:str):
    return User.objects.filter(username=username).first()



def create_user(validated_data):
    user = User.objects.create_user(
        username=validated_data["username"],
        password=validated_data["password"]
    )
    return user



def authenticated_user(username:str,password:str):

    user = get_user_by_name(username=username)
    if user is None or not user.check_password(password):
        return None

    return user


@transaction.atomic
def create_token(user:User):
    expire_at = timezone.now() + timedelta(days=7)

    user_token = UserToken.objects.filter(user=user).first()

    token = str(uuid.uuid4())
    if user_token:
        user_token.token = token
        user_token.expires_at = expire_at
        user_token.save()
    else:
        user_token = UserToken.objects.create(user=user,token=token,expires_at=expire_at)

    return user_token


@transaction.atomic
def record_user_login(user:User):
    today = timezone.localdate()
    login_log, created = UserLoginLog.objects.get_or_create(
        user=user,
        login_date=today,
        defaults={"login_at": timezone.now()},
    )
    if not created:
        login_log.login_at = timezone.now()
        login_log.save(update_fields=["login_at"])
    return login_log


@transaction.atomic
def update_user(user:User, validated_data):
    for field, value in validated_data.items():
        setattr(user, field, value)
    user.save()
    return user



@transaction.atomic
def change_user_password(*, user:User, validated_data):
    if not user.check_password(validated_data["old_password"]):
        return False
    user.set_password(validated_data["new_password"])
    user.save(update_fields=["password"])
    return True


