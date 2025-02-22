from django.db import models


# Create your models here.
class Role(models.Model):
    ROLES = {
        "a": "admin",
        'u': "user"
    }
    short_role = models.CharField(max_length=1, choices=ROLES)
    full_role = models.CharField(max_length=100, choices=ROLES)

    def __str__(self):
        return self.short_role, self.full_role


class Admin(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
