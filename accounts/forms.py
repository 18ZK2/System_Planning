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

'''class ChkForm(forms.Form):
     labels = ['チェック','複数チェック','ラジオボタン','動的選択肢１','動的選択肢２']
     CHOICE = [
             ('1',  '出勤'),
              ('2',  '社用外出'),
              ('3',  '私用外出'),
              ('4',  '遅刻'),
              ('5',  '早退'),
              ('6',  '休み'),
              ('7',  '午前休'),
              ('8',  '午後休'),
              ('9',  'テレワーク'),
              ('10', '退社'),
              ('11', '出張'),
            ]
     
     three = forms.MultipleChoiceField(
          label=labels[2],
          required=False,
          disabled=False,
          initial=['2'],
          choices=CHOICE,
          widget=forms.RadioSelect(attrs={
               'id': 'three','class': 'form-check-input'}))'''
        