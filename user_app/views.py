from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,'user_app/home.html')



def register_req(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,"successfull")
            return redirect('home')
        messages.error(request,"NO ......")
    form = NewUserForm()
    return render(request,'user_app/register.html',{'register_form':form})

def login_req(request):
    if request.method == "POST":
        form =AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user= authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"Welcome{username}")
                return redirect('user_app:home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"sorry????")
    form = AuthenticationForm()
    
    return render(request,'user_app/login.html',{'login_form':form, 'msg':messages})                 



def logout_req(request):
    logout(request)
    messages.info(request,"googby see you soon")
    return redirect('user_app:home')