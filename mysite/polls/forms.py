from django import forms


class MyForm(forms.Form):
    my_string = forms.CharField(max_length=100)

