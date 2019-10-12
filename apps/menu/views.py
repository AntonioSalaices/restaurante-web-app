from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate, get_user_model
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest    
from django.contrib import messages
from django.views.generic import TemplateView
from apps.menu.forms import LoginForm
# Create your views here.

def index(request):
    return render(request, "index.html")

@login_required(login_url='/login/')
def vista_logout(request):
    logout(request)
    return redirect('index')


def vista_login(request):
    form  = LoginForm(request.POST or None)
    context = {"form":form}
    if request.user.is_authenticated:
        return redirect('index')
    if form.is_valid():
        username= form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('index')
    return render(request,"usuarios/login.html",context)
    

          