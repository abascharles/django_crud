from django.contrib import admin

# register modelo to be visible in backend
# remember to import model

from students.models import Student

# Register your models here.

admin.site.register(Student)

