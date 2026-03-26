from rest_framework import serializers

from .models import User


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "nickname",
            "avatar",
            "gender",
            "bio",
            "phone",
        ]


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=6)


class UserLoginSerializer(UserRegisterSerializer):
    pass


class UserUpdateSerializer(serializers.Serializer):
    nickname = serializers.CharField(max_length=50, required=False, allow_blank=True)
    avatar = serializers.URLField(required=False, allow_blank=True)
    gender = serializers.ChoiceField(choices=User.GENDER_CHOICES, required=False)
    bio = serializers.CharField(max_length=500, required=False, allow_blank=True)
    phone = serializers.CharField(max_length=20, required=False, allow_blank=True)


class UserChangePasswordSerializer(serializers.Serializer):
    oldPassword = serializers.CharField(source="old_password", write_only=True, min_length=6)
    newPassword = serializers.CharField(source="new_password", write_only=True, min_length=6)