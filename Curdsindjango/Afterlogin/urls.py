from django.views.generic import TemplateView
from django.urls import path
from . import views
from Afterlogin.views import Home,Add_details,Update_details,Edit_details

urlpatterns = [
    path('home',Home.as_view(),name='home'),
    path('add_details',Add_details.as_view(),name='add_details'),
    path('edit_details/<int:id>',Edit_details.as_view(),name='edit_details'),
    path('update_details/<int:id>',Update_details.as_view(),name='update_details'),
    path('delete<str:id>',views.Delete,name='delete'),
    path('logout',views.Logout,name='logout'),
    
]
