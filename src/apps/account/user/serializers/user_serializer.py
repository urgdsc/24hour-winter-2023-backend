from rest_framework import serializers

from apps.account.authentication.services import get_authorization_token
from apps.account.user.models import User


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ["password", "is_superuser", "is_staff", "is_active", "groups", "user_permissions", "last_modified"]

    def get_token(self, obj):
        return get_authorization_token(obj)


class UserProxySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]
