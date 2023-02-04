from django.urls import path, include
from . import views

urlpatterns = [
    path("programs/", include([
        path("", views.ProgramListView.as_view(), name="program-list"),
        path("<str:id>", views.ProgramDetailView.as_view(), name="program-detail"),
    ])),
    path("universities", views.UniversityListView.as_view(), name="university-list"),
]
