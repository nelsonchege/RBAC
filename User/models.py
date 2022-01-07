from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class MainUsers(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def save(self):
        password = self.password
        self.password = make_password(password)
        super().save()

    def __str__(self):

        return self.username

class SubUsers(models.Model):
    mainUser = models.ForeignKey(MainUsers,on_delete=models.CASCADE,related_name="user")
    username = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.username
    