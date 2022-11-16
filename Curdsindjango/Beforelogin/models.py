from django.db import models

# Create your models here.

class Registration(models.Model):
    name  = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

    


# class User(models.Model):
# # username field
#     username = models.CharField(max_length=30, blank=False, null=False)
# # password field
#     password = models.CharField(max_length=8, blank=False, null=False)