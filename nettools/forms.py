#-*- coding: utf-8 -*-
from django import forms

class fileForm(forms.Form):
    file_location = forms.FileField()
