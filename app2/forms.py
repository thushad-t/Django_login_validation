from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields


class updateform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
