from django import forms


class MainForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label='Your password goes here')
