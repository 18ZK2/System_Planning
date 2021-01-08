# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy 
from django.http import HttpResponse
from . import forms
from . import models
from .models import EmployeeState
from .models import RoomCheck
from django.template import context
import sqlite3
from django.contrib.auth.decorators import login_required
from accounts.forms import SearchForm
from accounts.dbManage import NameSearch,TableInfo

def index(request):
    return render(request, "accounts/index.html")

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"


class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "accounts/logout.html"

@login_required
def index2(request):
    username = request.user.userID
    data = EmployeeState.objects.all().filter(userID=username)
    data2 = RoomCheck.objects.all().filter(userID=username)
    params = {'data': data, 'data2':data2}
    return render(request, "accounts/index2.html",params)

@login_required
def StateView(request):
    template_name = "accounts/state.html"

    if request.method == "POST":
        
        state = request.POST.get('state', '0')
        username = request.user.userID

        EmployeeState.objects.filter(userID=username).delete()

        EmployeeState.objects.update_or_create(
            userID=username,
            EMPstate=state,
        )
        return redirect("index2")

    else:
        return render(request, template_name)


    return(request, template_name)

def search(request):
    url = 'accounts/search.html'
    f = SearchForm()
    result =''
    if(request.method =='POST'):
        #入力が入ってきた
        f=SearchForm(request.POST)
        #値があるなら
        if(f.is_valid()):
            res = f.cleaned_data
            result = NameSearch(res['nameSerchField'])
    return render(request,url,{'form':f,'searchResult':result})

@login_required
def CheckIn(request):
    template_name = "accounts/shirahama1f.html"
    username = request.user.userID
    data = EmployeeState.objects.all()
    data2 = RoomCheck.objects.all()
    params = {'data': data, 'data2':data2}

    if request.method == "POST":
        
        room = request.POST.get('get_room_name', '0')
        username = request.user.userID

        RoomCheck.objects.filter(userID=username).delete()

        RoomCheck.objects.update_or_create(
            userID=username,
            RoomID=room,
        )
        return redirect("index2")

    else:
        return render(request, template_name, params)


    return(request, template_name, params)
