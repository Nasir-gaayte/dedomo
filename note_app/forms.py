from django import forms
from note_app.models import Users_model
from django.core import validators


class UserData(forms.ModelForm):
    class Meta():
        model = Users_model
        fields = ['username', 'email', 'first', 'family', 'note']
        