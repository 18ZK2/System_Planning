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
from accounts.forms import RadioForm
from accounts.forms import SearchForm

from .dbManage import NameSearch


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

#コネクトしなくてもデータベース使えます！
@login_required
def StateView(request):
    template_name = "accounts/state.html"

    if request.method == "POST":
        EMPstate = request.POST.get('state', '0')
        username = request.user.userID

        EmployeeState.objects.update_or_create(
            userID=username,
            EMPstate=state,
        )

        return HttpResponse("入力完了")

    else:
        return render(request, template_name)


    return(request, template_name)

def state(request):
    form = RadioForm
    return render(request, "accounts/state.html", {"form" : form})

def search(request):
    url = 'accounts/search.html'
    f = SearchForm()
    if(request.method =='POST'):
        #入力が入ってきた
        f=SearchForm(request.POST)
        if(f.is_valid()):
            res = f.cleaned_data
            print(res)
            result = NameSearch(res['nameSerchField'])
            print(result)
    return render(request,url,{'form':f})
