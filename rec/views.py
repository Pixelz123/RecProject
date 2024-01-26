from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rec.models import Experience
from django.contrib import messages

# Create your views here.
def home(request):
    user=request.user
    return render(request,'index.html',{'CurrentUser':user})

def signup(request):
    if request.method=='POST':
     try:
        if request.POST['password'] != request.POST['password_c']:
            messages.error(request,"password confirmation error")
            return render(request,"signup.html")
        user = User.objects.create_user(request.POST['Username'], request.POST['email'], request.POST['password'])
        user.save()
        login(request,user)
        return redirect('home')
     except:
        messages.error(request,"Invalid credentials...")
        return render (request,'signup.html')
    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
     user=authenticate(username=request.POST['Username'] ,password=request.POST['password'])
     if user is not None:
        login(request,user)
        return redirect('home')
    messages.error(request,"Invalid credentials..")
    return render(request,'signin.html')

def signout(request):
    logout(request)
    user=request.user
    print(user.username)
    return redirect('home')

def getExpList(request,id):
    if  id=="All":
     exp=Experience.objects.all()
     return render(request,'experience.html',{'Experience':exp,'CurrentUser':request.user,'filter':id})
    elif id=="Internship":
     exp=Experience.objects.filter(role='Internship')
     return render(request,'experience.html',{'Experience':exp,'CurrentUser':request.user,'filter':id})
    elif id=="FTE":
     exp=Experience.objects.filter(role='FTE')
     return render(request,'experience.html',{'Experience':exp,'CurrentUser':request.user,'filter':id})
    return render(request,'experience.html',{'Experience':exp,'CurrentUser':request.user,'filter':id})

def getExpDetails(request,id):
    exp=Experience.objects.filter(serial=id)
    return render (request,"experience_details.html",{'Experience':exp,'CurrentUser':request.user})

def addexperience(request):
     if request.method=='POST':
         
         ttl=request.POST['tte']
         det=request.POST['details']
         rol=request.POST['role']
         dte=request.POST['date']
         cmp=request.POST['org']
         authr=request.user.username
         ser=Experience.objects.all().count()+1
         exp=Experience.objects.create(title=ttl,content=det,date=dte,author=authr,role=rol,serial=ser,org=cmp)
         exp.save()
         return redirect(home)
     return render (request,"experience_add.html",{'CurrentUser':request.user})



