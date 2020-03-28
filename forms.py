from django import forms
from .models import Post, Login

class loginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = ('author', 'password',)
