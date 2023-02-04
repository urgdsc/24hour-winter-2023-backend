from django.urls import path
from . import views

urlpatterns = [
    path("programs", views.ProgramListView.as_view(), name="program-list"),
    path("universities", views.UniversityListView.as_view(), name="university-list"),
]
