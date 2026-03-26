from django.shortcuts import render

from typing import cast
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.authentication import BearerTokenAuthentication
from utils.response import success_response
from .models import User
from .serializers import (
    UserAuthResponseSerializer,
    UserChangePasswordSerializer,
    UserInfoSerializer,
    UserLoginSerializer,
    UserRegisterSerializer,
    UserUpdateSerializer,
)
from .services import (
    authenticated_user,
    change_user_password,
    create_token,
    create_user,
    record_user_login,
    update_user,
)




class UserRegisterAPIView(APIView):
    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = create_user(validated_data=serializer.validated_data)
        token = create_token(user=user)
        record_user_login(user=user)

        auth_payload = {
            "token":token.token,
            "expires_at":token.expires_at,
            "user":user
        }
        output = UserAuthResponseSerializer(auth_payload)
        return success_response(data=output.data)




class UserLoginAPIView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticated_user(**serializer.validated_data)
        if not user:
            raise ValidationError("wrong username or password")

        token = create_token(user=user)
        record_user_login(user=user)

        auth_payload = {
            "token":token.token,
            "expires_at":token.expires_at,
            "user":user
        }

        output = UserAuthResponseSerializer(auth_payload)
        return success_response(data=output.data)




class UserInfoAPIView(APIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return success_response(
            data=UserInfoSerializer(request.user).data
        )



class UserUpdateAPIView(APIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self,request):
        current_user = request.user
        serializer = UserUpdateSerializer(data=current_user)
        serializer.is_valid(raise_exception=True)

        user = update_user(user=current_user,validated_data=serializer.validated_data)

        return success_response(data=UserInfoSerializer(user).data)




class UserPasswordAPIView(APIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self,request):
        serializer = UserChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        changed = change_user_password(user=request.user,validated_data=serializer.validated_data)
        if not changed:
            raise ValidationError("wrong password")

        return success_response()





