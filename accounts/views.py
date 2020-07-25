from django.shortcuts import render, redirect
from django.contrib import messages, auth
import json
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('listings')

    if request.method == 'POST':
        email= request.POST['email']
        password = request.POST['psw']

        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Your are now logged in')
            return redirect('listings')
        else:
            messages.error(request,'Invalid username and password')
            return redirect('login')

    else:
        #return redirect('login')
        return render(request, 'accounts/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('listings')
        
    if request.method == 'POST':
        #LOGIN USER
        first_name= request.POST['fname']
        last_name= request.POST['lname']
        email= request.POST['email']
        password= request.POST['psw']
        # import pdb; pdb.set_trace()
        #if email already exists
        if User.objects.filter(email=email).exists():
           messages.error(request,'Account already exists')
           return redirect('register')
           #return render(request, 'accounts/register.html')
           #return HttpResponse({"error":"User already exists"}, content_type='application/json') 
        else:
            #looks good
            user = User.objects.create_user(
                email=email,
                username=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            # #login after register
            # auth.login(request,user)
            messages.success(request,'User created successfully')
            return redirect('login')
            # return HttpResponse(user, content_type='application/json')
             

    else:
        return render(request, 'accounts/register.html')


# @api_view(['GET', 'POST'])
# def register(request):
#     if request.method == 'POST':
#         print("hello")
#         data = json.dumps(
#             {
#                 "hello":"amogh"
#             }
#         )
#         return HttpResponse(data, content_type='application/json')

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    # import pdb; pdb.set_trace()
    return render(request, 'accounts/dashboard.html')