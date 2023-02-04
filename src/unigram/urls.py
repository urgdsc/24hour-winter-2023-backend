"""unigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admin import site
from django.http import HttpResponse
from django.urls import path, include
from django.utils.translation import gettext_lazy

site.site_title = gettext_lazy("Unigram")
site.site_header = gettext_lazy("Unigram")
site.index_title = gettext_lazy("Unigram")

admin.autodiscover()


def healthcheck(request):
    return HttpResponse(status=200)


urlpatterns = [
    path("healthcheck", healthcheck, name="healthcheck"),
    path("admin/", admin.site.urls),
    path("auth/", include("apps.account.authentication.urls")),
    path("user/", include("apps.account.user.urls")),
    path("", include("apps.university.urls")),
    path("", include("django_prometheus.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
