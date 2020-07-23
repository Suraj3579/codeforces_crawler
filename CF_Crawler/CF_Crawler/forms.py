from django import forms


class UserHandle(forms.Form):
    user_handle = forms.CharField(max_length=100)


class query_form(forms.Form):
    user_name = forms.CharField(max_length=30,help_text='Your Name',widget=forms.TextInput(attrs ={"class":'form-control',"placeholder":'Name'}))
    user_email = forms.CharField(max_length=254,help_text='Your Email Address',widget=forms.TextInput(attrs ={"class":'form-control',"placeholder":'Email Address'}))
    query_subject = forms.CharField(max_length=300,help_text='Enter Query Subject',widget=forms.TextInput(attrs ={"class":'form-control',"placeholder":'Query Subject'}))
    query_text = forms.CharField(max_length=2000,help_text='Enter Query here',widget=forms.Textarea(attrs ={"class":'form-control', "placeholder":'Type Your Query Here'}))
