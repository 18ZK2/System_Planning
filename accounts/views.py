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

    if request.method == "POST":
        EMPstate = request.POST.get('state', '0')

        conn = sqlite3.connect(r'D:\virtual\venv4\myproject\db.sqlite3') #DBへ接続
        c = conn.cursor()
        username = request.user.userID

        c.execute("INSERT INTO accounts_EmployeeState(userID) values(username)")
        c.execute("INSERT INTO accounts_EmployeeState(EMPstate) values(EMPstate) ")
        conn.commit()    #セーブ
        conn.close()     #DBとの接続をきる
        return HttpResponse("入力完了")

    else:
        return render(request, template_name)


    request(request, template_name)