from urllib import request
from venv import create
from . models import Car
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import logout
#from . models import authentication_not_required


# Create your views here.
# classbase view
class Home(View):
    #@authentication_not_required
    def get(self,request):
        emp = Car.objects.all()
        context={
            'emp':emp
        }
        return render(request,'home.html',context)

class Add_details(View):
    def get(self,request):
        return render(request,'add_car_details.html')

    def post(self,request):
        Car_name = request.POST.get('Car_name')
        model = request.POST.get('model')
        price = request.POST.get('price')
        brand = request.POST.get('brand')
        emp = Car(
            Car_name=Car_name,
            model=model,
            price=price,
            brand=brand,
        )
        emp.save()
        return redirect('home')
    
class Edit_details(View):
    def get(self,request,id):
        emp = Car.objects.filter(id=id)
        context={
            'emp':emp
        }
        return render(request,'edit.html',context)
    
    def post(self,request,id):
        Car_name = request.POST.get('Car_name')
        model = request.POST.get('model')
        price = request.POST.get('price')
        brand = request.POST.get('brand')
        emp = Car(
            id=id,
            Car_name=Car_name,
            model=model,
            price=price,
            brand=brand,
        )
        emp.save()
        return redirect('home')
    

class Update_details(View):
    def get(self,request):
        return render (request,'home.html')

    
#funtion base view  
def Delete(request,id):
    emp = Car.objects.get(id=id)
    emp.delete()
    return redirect('home')


def Logout(request):
    logout(request)
    return render(request,'login.html')

