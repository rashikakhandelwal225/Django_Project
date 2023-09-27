from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
    # fm = StudentRegistration(auto_id=True)
    # fm = StudentRegistration(auto_id='some_%s', label_suffix=' ', initial={'name': 'Sonam', 'email':'sonam@gmail.com'})
    # fm = StudentRegistration(auto_id=False)
    fm = StudentRegistration()   #creating the data/class object
    fm.order_fields(field_order=['email','name', 'first_name'])   #Changing the order of the fields
    return render(request,'enroll/userregistration.html', {'form':fm})
