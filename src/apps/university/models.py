from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class University(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, editable=False, default=uuid4)

    name = models.CharField(verbose_name=_("Name"), max_length=256, null=False, blank=False)
    description = models.TextField(verbose_name=_("Description"), max_length=1024, null=True, blank=True)
    location = models.CharField(verbose_name=_("Location"), max_length=256, null=False, blank=False)

    website = models.URLField(verbose_name=_("Website Address"), null=True, blank=True)

    is_verified = models.BooleanField(
        verbose_name=_("Is Verified"),
        help_text=_("Weather the data is verified by the institution"),
        default=False
    )

    date_created = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)
    last_modified = models.DateTimeField(verbose_name=_("Last modified"), auto_now=True)

    class Meta:
        verbose_name = _("University")
        verbose_name_plural = _("Universities")

    def __str__(self) -> str:
        return f"{self.name}"


class Program(models.Model):
    class Level(models.TextChoices):
        CERTIFICATE = "CERTIFICATE", _("Certificate")
        DIPLOMA = "DIPLOMA", _("Diploma")
        BACHELOR = "BACHELOR", _("Bachelor")
        MASTER = "MASTER", _("Master")
        PHD = "PHD", _("PhD")

    id = models.UUIDField(primary_key=True, auto_created=True, editable=False, default=uuid4)

    university = models.ForeignKey(
        verbose_name=_("University"),
        to="university.University",
        on_delete=models.CASCADE,
        related_name="programs"
    )

    level = models.CharField(
        verbose_name=_("Level"), max_length=16, choices=Level.choices, null=False, blank=False, default=Level.BACHELOR
    )

    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(max_length=1024, null=True, blank=True)

    duration = models.PositiveIntegerField(
        verbose_name=_("Duration"),
        help_text=_("Duration in years, based on 2 semesters a year with 5 courses each."),
        null=False,
        blank=False,
        default=4
    )

    domestic_annual_tuition = models.PositiveIntegerField(
        verbose_name=_("Domestic Annual Tuition"),
        help_text=_("Average annual tuition based on 5 courses per each semester.")
    )
    international_annual_tuition = models.PositiveIntegerField(
        verbose_name=_("International Annual Tuition"),
        help_text=_("Average annual tuition based on 5 courses per each semester.")
    )

    date_created = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)
    last_modified = models.DateTimeField(verbose_name=_("Last modified"), auto_now=True)

    class Meta:
        verbose_name = _("Program")
        verbose_name_plural = _("Programs")

    def __str__(self) -> str:
        return f"{self.name} | {self.university.name}"
