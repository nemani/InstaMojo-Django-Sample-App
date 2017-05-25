from django import forms

class PayForm(forms.Form):
    Name = forms.CharField(label='Your name', max_length=100)
    Email = forms.EmailField(label='Email Address')
    Phone = forms.IntegerField(label='Phone Number', min_value=7000000000, max_value=9999999999)
    Amount = forms.IntegerField(label='Amount')
    Purpose = forms.CharField(label="Purpose", max_length=100)
