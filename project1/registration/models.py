from django.db import models

class registration(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class login(models.Model):
    Username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField()

    def __str__(self):
        return self.Username