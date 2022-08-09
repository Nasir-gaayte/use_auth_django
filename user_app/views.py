from configparser import LegacyInterpolation
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