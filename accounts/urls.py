from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = "index"),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView, name="logout"),
    path('index2/',views.index2, name="index2"),
    path('state/',views.StateView, name = "state"),
]