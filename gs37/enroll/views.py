from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        print(fm)
        print('This is from POST request')
        print('Clean Data',fm.cleaned_data)
        if fm.is_valid():
            print('Clean Data',fm.cleaned_data['name'])
            password = fm.cleaned_data['password']
            print('password', password)
        # we can redirect it on another page as well
        fm = StudentRegistration()
    else:
        fm =StudentRegistration()
        print('This is GET request')
    return render(request, 'enroll/userregistration.html', {'form':fm})
    
