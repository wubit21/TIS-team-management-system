from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import user_input
#data input form
class inputForm(ModelForm):
 class Meta:
  model= user_input
  fields="__all__"
#register form

class registerForm(UserCreationForm):
    username = forms.CharField(max_length = 100)
    #email  = forms.EmailField(max_length = 100)
    password1 = forms.CharField(widget = forms.PasswordInput() , max_length = 100)
    password2 = forms.CharField(widget = forms.PasswordInput(),  max_length = 100)
    first = forms.CharField(max_length = 100 )
    last = forms.CharField(max_length = 100)
    email = forms.EmailField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( "first","last","username", "email", "password1","password2")
    
    def save(self, commit=True):
        user = super(registerForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user
#to register Admin
class adminRegisterForm(UserCreationForm):
    username = forms.CharField(max_length = 100)
    #email  = forms.EmailField(max_length = 100)
    password1 = forms.CharField(widget = forms.PasswordInput() , max_length = 100)
    password2 = forms.CharField(widget = forms.PasswordInput(),  max_length = 100)
    first = forms.CharField(max_length = 100 )
    last = forms.CharField(max_length = 100)
    email = forms.EmailField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( "first","last","username", "email", "password1","password2")
    
    def save(self, commit=True):
        user = super(adminRegisterForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.is_staff = True
        if commit:
            user.save()
        return user
