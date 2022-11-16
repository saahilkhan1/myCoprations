from django.views import View
from django.urls import path
from . import views
from Beforelogin.views import Login,Register
from django.views.generic import TemplateView

urlpatterns = [
    path('',Login.as_view(),name='login'),
    path('base',views.Base,name='base'),

    path('register',Register.as_view(),name='register'),
]


# from django.contrib import admin
# from django.urls import path

# from Beforelogin.views import home_view

# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', home_view, name='home'),
# ]