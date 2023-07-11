from django.contrib import admin
from enroll.models import Student
# Register your models here.

@admin.register(Student)     #decorator
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','stuid', 'stuname', 'stuemail', 'stupass')
    #list_display=('id',)    to display single field 

# admin.site.register(Student, StudentAdmin)

