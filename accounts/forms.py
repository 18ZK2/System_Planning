from django.contrib.auth import forms as auth_forms
from django.contrib.admin import widgets
from django import forms
import os
import sqlite3

class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

class SearchForm(forms.Form):

    nameSearchField =forms.CharField(label='ゆーざーIDから状態',required=False,)
    placeSearcField =forms.IntegerField(label='出勤場所からユーザーID',required=False,)

class MakeMapForm(forms.Form):

    slicedMaps = forms.CharField(widget=forms.Textarea)
class MapNameForm(forms.Form):

    name = forms.CharField(label='部屋名',required=False,)