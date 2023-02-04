from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from apps.university.models import Program
from apps.university.serializers import ProgramSerializer


class ProgramListView(ListAPIView):
    """
    Returns a list of all programs
    """

    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        "name",
        "description",
        "duration",
        "university__name",
        "university__location",
    ]
    search_fields = [
        "name",
        "description",
        "duration",
        "university__name",
        "university__location",
        "international_annual_tuition__lte",
    ]
