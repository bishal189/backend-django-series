
from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import Musician,Album

def home(request):
    album=Album.objects.all().order_by('-id')

    context={
        'dinesh':album
    }
    return render(request,'home.html',context) 


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



def logout_view(request):

    logout(request)
    return redirect('login')



def album_view(request):
    if request.method == 'POST':
        name=request.POST['name']
        date=request.POST['date']
        rating=request.POST['rating']
        image=request.FILES['file']
        musicain=Musician.objects.get(id=1)
        try:
            # album=Album.objects.create(artist=musicain,name=name,release_date=date,num_stars=rating,album_image=image)
            album=Album() 
            album.artist=musicain
            album.name=name
            album.release_date=date
            album.num_stars=rating
            album.album_image=imag
            album.save()
            return redirect('home')

        except: 
            return redirect('album')
        
    else: 
        return render(request,'album.html')