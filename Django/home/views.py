
from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,'home.html') 


def register(request):
    # code 
    if request.method=="POST":
        print(request.POST)
        # <QueryDict: {'csrfmiddlewaretoken': 
        # ['dQ6V7MYwnmMXE3U5xOT9VYgaprjZjccHMPJyQWb70kenjLDirM74XpKWncpBIZt7'], 'username': ['abc'], 
        # 'email': ['abc@gmail.com'], 'password': ['abc'], 'confirm_password': ['abc']}>


        #getting data from the user(fronted )
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        #checking password and confrim password

        if password!=confirm_password:
            return redirect('register')
        
        # create user on the database
        # saving credentials on the db 
        
        #create user
        user=User.objects.create_user(username=username,email=email,password=password)
        #table user stored
        user.save()
        #login page janey 
        return redirect('login')

    else:
        return render(request,'register.html')


def login_view(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        #username getting
        username=User.objects.get(email=email).username
        # check credentails withdatabase
        user=authenticate(request,username=username,password=password)
        
        # yedi user ko value true xa vaney 
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('register')   
    
    return render(request,'login.html')