from ast import Import, Return
from email import message
from re import template
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from.models import Notice, Comment
from  django.contrib.auth.decorators import login_required
from .forms import CommentForm





# Create your views here.



def index(request):
    return render(request,'base/index.html')

@login_required(login_url = 'login')
def home(request):
    if request.user is None: 
        return redirect('/') 
    else:
        notices = Notice.objects.all()
        return render(request, 'base/home.html',{'notices': notices})
    


#Comment function

@login_required(login_url = 'login')
def comment(request, pk):
    notice = Notice.objects.get(id=pk)
    comments = Comment.objects.filter(notice=notice)
    form = CommentForm
    contex ={
            'notice':notice,
            'comments':comments,
            'form':form,
           }
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.notice = notice
            obj.save()
            return render(request, 'base/notice-detail.html', contex)
           
    else:
        form= CommentForm()
        
    return render(request, 'base/notice-detail.html', contex)



       
#Rgister function

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST': 
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            
            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email Already Taken')
                    return redirect('register')
                elif User.objects.filter(username=username).exists():
                    messages.info(request,'Username Already Used')
                    return redirect('register')
                else:
                    user = User.objects.create(username = username, email = email, password = password)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request,'Password not matched')
                return redirect('register')
        else:
            return render(request,'auth/register.html')
    
    
    #Login Function
    
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            
            user = auth.authenticate(username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Invalid user')
                return redirect('login')
        else:    
            return render(request, 'auth/login.html')
       
#logout function
def logout(request):
        auth.logout(request)
        return redirect('/')