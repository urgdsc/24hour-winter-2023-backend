from django.contrib import admin

from apps.university.models import University, Program


# Register your models here.
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    pass


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    pass
