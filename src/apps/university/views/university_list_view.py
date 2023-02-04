from rest_framework.generics import ListAPIView

from apps.university.models import University
from apps.university.serializers import UniversitySerializer


class UniversityListView(ListAPIView):
    """
    Returns a list of all universities
    """

    serializer_class = UniversitySerializer
    queryset = University.objects.all()
    search_fields = [
        "name",
        "description",
        "location",
        "programs__name",
    ]
