
from django.shortcuts import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html') 


def register(request):
    # code 
    if request.method=="POST":
        print(request.POST)
        # <QueryDict: {'csrfmiddlewaretoken': 
        # ['dQ6V7MYwnmMXE3U5xOT9VYgaprjZjccHMPJyQWb70kenjLDirM74XpKWncpBIZt7'], 'username': ['abc'], 
        # 'email': ['abc@gmail.com'], 'password': ['abc'], 'confirm_password': ['abc']}>

        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        print(username,email,password,confirm_password)



    else:
        return render(request,'register.html')


def login(request):
    return render(request,'login.html')