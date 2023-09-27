from django.core import validators
from django import forms

def starts_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Name should start with s')

class StudentRegistration(forms.Form):
    # name = forms.CharField(widget=forms.PasswordInput())
    # name = forms.CharField(widget=forms.HiddenInput)
    # name = forms.CharField(widget=forms.Textarea)
    # name = forms.CharField(widget=forms.CheckboxInput)
    # name = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1', 'id':'uniqueid'}))
    # name = forms.CharField()
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)

    # name = forms.CharField()
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) <4:
    #         raise forms.ValidationError('Enter more than or equal to 4 chars')
    #     return valname
    
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    name = forms.CharField(validators=[starts_with_s])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label = 'Password(again)',widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpwd = self.cleaned_data['password']
        valrpwd = self.cleaned_data['rpassword']
        if valpwd != valrpwd:
            raise forms.ValidationError('Password does not match')

