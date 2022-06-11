from django.db import models
from accounts.models import UserAccount

# Create your models here.
class Society(models.Model):
    name = models.CharField(max_length=54)
    organization_name = models.CharField(max_length=54)
    location = models.CharField(max_length=125)
    users = models.ForeignKey(UserAccount, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
