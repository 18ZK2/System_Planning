# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy 
from django.http import HttpResponse, request
from . import forms
from . import models
from .models import EmployeeState
from django.template import context
import sqlite3
from django.contrib.auth.decorators import login_required
from .forms import SearchForm,MakeMapForm,MapNameForm
from .dbManage import StateSearch,PlaceSearch,TableInfo,empStateDic,RatestMapNum,SelectMap
from .AddMap import CheckinMaps,BuildHTML
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

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
    print(data)
    params = {'data': data}
    return render(request, "accounts/index2.html",params)

@login_required
def StateView(request):
    template_name = "accounts/state.html"

    if request.method == "POST":
        
        state = request.POST.get('state', '0')
        username = request.user.userID

        '''EmployeeState.objects.filter(userID=username).delete()
        EmployeeState.objects.update_or_create(
            userID=username,
            EMPstate=state,
        )'''

        S = EmployeeState.objects.filter(userID=username).first()
        S.EMPstate = state
        S.save()

        return redirect("index2")

    else:
        return render(request, template_name)


    return(request, template_name)

def Search(request):
    url = 'accounts/search.html'
    f = SearchForm()
    result = ['','']
    if(request.method =='POST'):
        #入力が入ってきた
        f=SearchForm(request.POST)
        #値があるなら
        if(f.is_valid()):
            res = f.cleaned_data
            result = [StateSearch(res['nameSearchField']),PlaceSearch(res['placeSearcField'])]
    return render(request,url,
                  {'form':f,'searchResult':result[0],'placeResult':result[1]})

@login_required
def CheckIn(request):
    #部屋の場所変更
    template_name = "accounts/shirahama1f.html"
    username = request.user.userID
    data = EmployeeState.objects.all()
    params = {'data': data}

    if request.method == "POST":
        
        room = request.POST.get('get_room_name', '0')
        username = request.user.userID

        S = EmployeeState.objects.filter(userID=username).first()
        S.RoomID = room
        S.save()

        return redirect("index2")

    else:
        return render(request, template_name, params)


    return(request, template_name, params)

def CheckIn2(request):
    #部屋の場所変更
    template_name = "accounts/shirahama2f.html"
    username = request.user.userID
    data = EmployeeState.objects.all()
    params = {'data': data}

    if request.method == "POST":
        
        room = request.POST.get('get_room_name', '0')
        username = request.user.userID

        S = EmployeeState.objects.filter(userID=username).first()
        S.RoomID = room
        S.save()
        
        return redirect("index2")

    else:
        return render(request, template_name, params)


    return(request, template_name, params)

def MakeMaps(request):
    #マップ追加
    url = 'accounts/makeMaps.html'
    f = MakeMapForm()
    if(request.method =='POST'):
        #イメージマップジェネレータからもらってきた
        f = MakeMapForm(request.POST)
        print(f)
        cm = CheckinMaps()
        slicedTexts = cm.SplitTexts(f.cleaned_data['slicedMaps'])
        cm.NumberingImagemapShapes(slicedTexts)
        

    return render(request,url,{'form':f})

@csrf_exempt
def ShowMap(request):
    m = BuildHTML()
    s = SelectMap(0,6)
    
    return HttpResponse(m.Build('/static/pics/test.png',m.MakeMap(s)))


class RoomsView(ListView, LoginRequiredMixin):
    model = EmployeeState

    def get_queryset(self):

        if 'name' in self.request.GET:
            q_word = self.request.GET.get('name')
            object_list = EmployeeState.objects.filter( Q(userID__icontains=q_word) ) 

        elif 'state' in self.request.GET:
            q_word = self.request.GET.get('state')
            object_list = EmployeeState.objects.filter( Q(EMPstate__iexact=q_word) )

        elif 'room' in self.request.GET:
            q_word = self.request.GET.get('room')
            object_list = EmployeeState.objects.filter( Q(RoomID__iexact=q_word) )

        else:
            object_list = EmployeeState.objects.all()
        return object_list