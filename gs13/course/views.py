from django.shortcuts import render
from datetime import datetime

# Create your views here.
def learn_django(request):
    # # return render(request, 'course/courseone.html', {'nm':'Django'})
    # cname = 'Django'
    # duration = '4 Months'
    # seats = 10
    # text = 'django is awesome'
    # django_details = {'nm':cname, 'du':duration, 'st':seats , 'txt': text}
    # return render(request, 'course/courseone.html', django_details)
    # d = datetime.now()
    # return render(request, 'course/courseone.html', {'dt':d})
    # return render(request, 'course/courseone.html', {'nm':True})
    # stu = {'stu1':{'name': 'Rahul','roll':101},
    #        'stu2': {'name':'Sonam', 'roll':102},
    #        'stu3': {'name': 'Raj', 'roll': 103},
    #        'stu4': {'name':'Anu', 'roll':104},
    data = {'stu1':{'name': 'Rahul','roll':101},
           'stu2': {'name':'Sonam', 'roll':102},
           'stu3': {'name': 'Raj', 'roll': 103},
           'stu4': {'name':'Anu', 'roll':104},
    }

    # students = {'student':stu}
    return render(request, 'course/courseone.html', {'data':data})
