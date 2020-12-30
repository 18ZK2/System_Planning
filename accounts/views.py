from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy 
from django.http import HttpResponse
from . import forms
from . import models
from .models import EmployeeState
from django.template import context
import sqlite3
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "accounts/index.html")

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"


class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "accounts/logout.html"

@login_required
def index2(request):
    return render(request, "accounts/index2.html")

@login_required
def StateView(request):
    template_name = "accounts/state.html"
    model = EmployeeState

    if request.method == "POST":
        EMPstate = request.POST.get('state', '0')
        userID = request.user

        conn = sqlite3.connect('../db.sqlite3') #DBへ接続
        c = conn.cursor()
        c.execute( "INSERT INTO EmployeeState value( userID, EMPstate)")
        conn.commit()  #セーブ
        conn.close     #DBとの接続をきる
        return (template_name)

    else:
        return render(request, template_name)


    request(request, template_name)