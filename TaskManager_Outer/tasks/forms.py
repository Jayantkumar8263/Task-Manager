from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserCreationform(UserCreationForm):
    email = forms.EmailField(required = True)
    
    class Meta: # here we used meta for increasing the funtionality of the class, for adding extra fields to it. 
        model = User 
        fields = ("username", "email", "password1", "password2")