from django.db import models


class Household(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    household = models.ForeignKey(
        Household, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name
