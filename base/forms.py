from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from .models import Record
from django.forms.widgets import PasswordInput, TextInput

#create user

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


#user login
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



#add a record form
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields =['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'region', 'country']


#update a record form
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields =['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'region', 'country']