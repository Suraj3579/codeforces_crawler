from django import forms


class UserHandle(forms.Form):
    user_handle = forms.CharField(max_length=100)
