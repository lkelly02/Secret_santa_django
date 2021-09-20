from django.db import models

# A model to represent a household of n number of members


class Household(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=True)

    def __str__(self) -> str:
        return self.name

# A model to represent each individual member of a Household. Each household member can only have 1 household.


class HouseholdMember(models.Model):
    name = models.CharField(max_length=255)
    email_address = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    household = models.ForeignKey(
        Household, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

# A model to represent an individual that is part of one big group.


class GroupMember(models.Model):
    name = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self) -> str:
        return self.name
