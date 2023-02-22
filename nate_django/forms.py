from django import forms


class user_reg(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField()


class user_login(forms.Form):
    username = forms.CharField(max_length=100)
    user_password = forms.CharField()


class members_reg(forms.Form):
    Name = forms.CharField(max_length=100)
    Age = forms.CharField(max_length=100)
    Phone = forms.CharField(max_length=100)
    City = forms.CharField(max_length=100)
    Country = forms.CharField(max_length=100)
