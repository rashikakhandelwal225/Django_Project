from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(initial='Rashika', help_text='we can show this text as a error msg or warning to the user')
    email = forms.EmailField()
    first_name = forms.CharField()
