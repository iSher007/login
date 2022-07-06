from django import forms
from django.contrib.auth.models import *


class SignUp(forms.ModelForm):
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()

        pass1 = cleaned_data.get("password")
        pass2 = cleaned_data.get("confirm_password")

        if pass2 != pass1:
            self.add_error(None, "Passwords are not same!")


class SignIn(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
