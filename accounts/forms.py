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

    nameSerchField =forms.CharField()
