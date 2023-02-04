from rest_framework.generics import RetrieveAPIView

from apps.university.models import Program
from apps.university.serializers import ProgramSerializer


class ProgramDetailView(RetrieveAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    lookup_field = "id"
