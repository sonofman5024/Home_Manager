from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=10)
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    hash_pass = models.CharField(max_length=50)
    claims = models.IntegerField()
    complaint = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return self.name
    


