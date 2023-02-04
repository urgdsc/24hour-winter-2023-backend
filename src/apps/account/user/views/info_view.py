from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from apps.account.user.serializers import UserSerializer


class UserInfoView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.serializer_class
        kwargs.setdefault(
            "context",
            {"request": self.request, "format": self.format_kwarg, "view": self},
        )
        return serializer_class(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return Response(self.get_serializer(instance=request.user).data, status=HTTP_200_OK)
