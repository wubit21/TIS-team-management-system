from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from account.models import user_input
from .forms import inputForm,registerForm,adminRegisterForm
from.models import user_input




def user_output(request):
    list=user_input.objects.all()
    return render(request,'authenticate/user_output.html',{'list':list})
def user_inputp(request):
    submitted=False
    if request.method == "POST":
     form = inputForm(request.POST,request.FILES)
     if form.is_valid():
        form.save()
        return HttpResponseRedirect('/user_input')
    else:
        form =  inputForm
        if 'submitted' in request.GET:
           submitted=True
           messages.success(request, "Report submitted!" )
    return render(request, 'authenticate/user_input.html', {'form':form ,'submitted' :submitted})
    
#TIS team user login
def login_user(request):
    submitted = False
    context={}
    if request.method == "POST":
     username = request.POST['username']
     password = request.POST['password']
     user = authenticate(request, username=username, password=password)
     if user is not None:
           login(request, user)
                    # Redirect to a success page.
           return redirect('user_input')
           messages.success(request, "Login successful." )
     else:
          return redirect('login')
    else:
          return render(request, 'authenticate/login.html', context)     
def home_screen_view(request):

    context= {}
    return render(request,"main/home.html", context)
def logout_user (request):
    logout(request) 
    return redirect('home') 
    
def register (request):
    
    if request.method == "POST":
        form=registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            username =form.cleaned_data['username']
            password=form.cleaned_data['password1']
            first=form.cleaned_data['first']
            last=form.cleaned_data['last']
            user = authenticate(username='username',password='password')
            messages.success(request, "Registration successful." )
            return redirect("register")
    else:
        form= registerForm()
    return render(request, 'authenticate/register.html',{'form':form })
   
'''   
#DELETE A USER
def deleteUser (request):

 context={}
 if request.method == "POST":
     username = request.POST['username']
     username = user.objects.filter(username)
     username.delete()
 else:
    return render(request, 'authenticate/deleteUser.html', context) 

    submitted = False
    context={}
    if request.method == "POST":
     username = request.POST['username']
     user = authenticate(request, username=username)
     if user is not None:
           login(request, user)
                    # Redirect to a success page.
           return redirect('home')
           messages.success(request, "Login successful." )
     else:
          return redirect('deleteUser')
    else:
          return render(request, 'authenticate/deleteUser.html', context)
'''
    #TIS admin login
def adminLogin(request):
    submitted = False
    context={}
    if request.method == "POST":
     username = request.POST['username']
     password = request.POST['password']
     user = authenticate(request, username=username, password=password)
     #if user.is_staff == True:
    
     if user is not None and user.is_staff == True:
           login(request, user)
                    # Redirect to a success page.
           return redirect('register')
           messages.success(request, "Login successful.")
       
     else:
          return redirect('adminLogin')
    else:
          return render(request, 'authenticate/adminLogin.html', context) 
#to register admin
def adminRegister (request):
    
    if request.method == "POST":
        form=adminRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username =form.cleaned_data['username']
            password=form.cleaned_data['password1']
            first=form.cleaned_data['first']
            last=form.cleaned_data['last']
            user = authenticate(username='username',password='password')
            messages.success(request, "Registration successful." )
            return redirect("adminRegister")
    else:
        form= adminRegisterForm()
    return render(request, 'authenticate/adminRegister.html',{'form':form })