from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    date_birth = models.DateField(null=True)
    is_kid = models.BooleanField('kid status', default = False)
    is_parent = models.BooleanField('parent status', default = False)