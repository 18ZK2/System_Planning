from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = "index"),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('index2/',views.IndexView.as_view(), name="index2"),
]