from django.shortcuts import render,redirect
#from .forms import RegistrationForm
from . models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views import View
# Create your views here.


def Base(request):
    return render(request,'base.html')


class Login(View):
    def get(self,request):                                                                                                                                                                                  #if request.method == "GET":
        return render(request,'login.html')
    
    def post(self,request): 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        print(user)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login') 
             
#   user_details = UserForm(request.POST)
#       if user_details.is_valid():
#             user_details.save()
#             return HttpResponse("Data submitted successfully")
#       else:
#             return render(request, 'home.html', {'form':user_details})
#   else:
#         form = UserForm(None)
#         return render(request, 'home.html', {'form':form})



class Register(View):
    def get(self,request):
        return render(request,'register.html')

    
        # if request.method == "POST":
            # details = RegistrationForm(request.POST)
            # if details.is_valid():
            #     details.save()
            #     return HttpResponse("Data submitted successfully")
            # else:
            #     details = RegistrationForm(None)
            # return render(request, 'login.html', {'form':details})
    def post(self,request):   
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = make_password(request.POST.get('password'))


        value={
            'name':name,
            'email':email,
            'phone':phone
        }
        #validation
        error_message = None
        if not name:
            error_message = "First name required"
        elif len(name) < 3:
            error_message = "Enter Atleast must be 4 character long"
        elif not email:
            error_message = "Email required"
        elif len(email) < 3:
            error_message = "Enter Valid Email"
        elif not phone:
            error_message = "Phone Number required"
        elif len(phone) < 10:
            error_message = "Enter Valid Number"
        elif not password:
            error_message = "Enter Password"
        elif len(password) < 3:
            error_message = "Enter Strong Password !!!"


        
        #data save 
        if not error_message:
            emp=Registration.objects.create(
                name=name,email=email,
                phone=phone,password=password)
            emp.save()
            return redirect('login')
        else:
            data={
                'error' : error_message,
                'values' : value
            }
            return render(request,'register.html',data)
                                                                                                                                                                                                                                                                                                                                              #  return render(request,'register.html')

                











# def Register(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         password = make_password(request.POST.get('password'))

#         emp=Registration.objects.create(name=name,email=email,phone=phone,password=password)
#         emp.save()
#         return redirect('login')

        
#     return render(request,'register.html')


# from django.shortcuts import render
# from django.http import HttpResponse

# from .forms import UserForm


# # Create your views here.
# def home_view(request):
#     if request.method == 'POST':
#         user_details = UserForm(request.POST)
#         if user_details.is_valid():
#             user_details.save()
#             return HttpResponse("Data submitted successfully")
#         else:
#             return render(request, 'home.html', {'form':user_details})
#     else:
#         form = UserForm(None)
#         return render(request, 'home.html', {'form':form})