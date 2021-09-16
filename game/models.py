from django.db import models


class Household(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=True)

    def __str__(self) -> str:
        return self.name


class HouseholdMember(models.Model):
    name = models.CharField(max_length=255)
    email_address = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    household = models.ForeignKey(
        Household, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class GroupMember(models.Model):
    name = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self) -> str:
        return self.name
