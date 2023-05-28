from django import forms 
from .models import DiffExpression, LinearAlgebra, Polynomial
from django.contrib.auth import get_user_model
User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RequestFriendForm(forms.Form):
    id = forms.CharField()

class AcceptForm(forms.Form):
    id = forms.CharField()

class UserFriendsForm(forms.Form):
    id = forms.CharField()

class DiffForm(forms.ModelForm):
    class Meta:
        model = DiffExpression
        fields = ['exp']

class PolyForm(forms.ModelForm):
   class Meta:
        model = Polynomial
        fields = ['exp']

class LalgForm(forms.ModelForm):
    class Meta:
        model = LinearAlgebra
        fields = ['exp']