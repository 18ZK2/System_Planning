from django.contrib.auth import forms as auth_forms
from django.contrib.admin import widgets
from django import forms
import os

class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label


CHOICE = {
    ('0','出勤'),
    ('1','社用外出'),
    ('2','私用外出'),
    ('3','遅刻'),
    ('4','早退'),
    ('5','休み'),
    ('6','午前休'),
    ('7','午後休'),
    ('8','テレワーク'),
    ('9','退社'),
    ('10','出張'),
}

class RadioForm(forms.Form):
    select = forms.ChoiceField(label='', widget=forms.RadioSelect, choices= CHOICE, initial=0)