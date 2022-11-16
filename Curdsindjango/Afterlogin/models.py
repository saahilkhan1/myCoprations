from django.db import models

# Create your models here.
class Car(models.Model):
    Car_name = models.CharField(max_length=200,null=True,blank=True)
    model = models.CharField(max_length=50,null=True,blank=True)
    price = models.CharField(max_length=50,null=True,blank=True)
    brand = models.CharField(max_length=70,null=True,blank=True)

    def __str__(self):
        return self.Car_name


# import functools
# from django.shortcuts import redirect
# from django.contrib import messages

# def authentication_not_required(view_func, redirect_url="login"):
                        
#     @functools.wraps(view_func)
#     def wrapper(request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return view_func(request,*args, **kwargs)
#         messages.info(request, "You need to be logged out")
#         print("You need to be logged out")
#         return redirect(redirect_url)
#     return wrapper



