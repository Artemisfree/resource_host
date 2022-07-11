from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from main_app.models import User


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')


# class HostForm(forms.ModelForm):
#     class Meta:
#         model = Host

#         fields = ('ip', 'port', 'resource_type')
