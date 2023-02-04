from rest_framework import serializers

from apps.university.models import Program
from apps.university.serializers import UniversitySerializer


class ProgramSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)

    class Meta:
        model = Program
        exclude = ["date_created", "last_modified"]
