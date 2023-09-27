from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.

def thankyou(request):
    return render(request, 'enroll/success.html', )



def showformdata(request):
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        print(fm)
        print('This is from POST request')
        print('Clean Data',fm.cleaned_data)
        if fm.is_valid():
            print('Form Validated')
            print('name :', fm.cleaned_data['name'])
            print('Roll:' ,fm.cleaned_data['roll'])
            print('Price:' ,fm.cleaned_data['price'])
            print('Rate:' ,fm.cleaned_data['rate'])
            print('Agree:', fm.cleaned_data['agree'])
            
        # we can redirect it on another page as well
        # return render(request, 'enroll/success.html', {'nm':name})
        return HttpResponseRedirect('/regi/success/')
    else:
        fm =StudentRegistration()
        print('This is GET request')
    return render(request, 'enroll/userregistration.html', {'form':fm})
    
