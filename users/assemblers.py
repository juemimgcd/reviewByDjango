from .serializers import UserInfoSerializer


def build_user_auth_response(*, token, user):
    return {
        "token": token.token,
        "expiresAt": token.expires_at,
        "userInfo": UserInfoSerializer(user).data,
    }
