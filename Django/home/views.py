
from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

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


def login(request):
    #code
    # getting data from user(email and password)
    #checking with db (exist or not)
    #return true or false if true then login
    #return false return to login
    #redirect to home page
    return render(request,'login.html')