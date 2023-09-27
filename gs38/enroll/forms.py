from django import forms
class StudentRegistration(forms.Form):
    # name = forms.CharField(widget=forms.PasswordInput())
    # name = forms.CharField(widget=forms.HiddenInput)
    # name = forms.CharField(widget=forms.Textarea)
    # name = forms.CharField(widget=forms.CheckboxInput)
    # name = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1', 'id':'uniqueid'}))
    # name = forms.CharField()
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)

    name = forms.CharField(min_length=5, max_length=50, strip= False, empty_value='Sonam', error_messages={'required':'Enter your name'})
    roll = forms.IntegerField(min_value=5, max_value=40)
    price = forms.DecimalField(min_value=5, max_value=40, max_digits=4, decimal_places=1)
    rate = forms. FloatField(min_value=5, max_value=40)
    agree=forms.BooleanField(label_suffix='',label='I Agree')