from django.contrib import admin
from django.urls import path,include 

admin.site.site_title = '管理メニュー'
admin.site.site_header = '管理メニュー'
admin.site.index_title = 'メニュー'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')), 
]
