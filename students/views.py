from django.shortcuts import render
from . models import Student


# Create your views here.

def home(request):
    return render(request, 'home.html', context={'navbar': 'home'})


def about(request):
    return render(request, 'about.html', context={'navbar': 'about'})


def contact(request):
    return render(request, 'contact.html', context={'navbar': 'contact'})

# I used this form to view data from database

def view(request):
    # import model you want to work with here
    # get all objects from model
    students = Student.objects.all()  # returns all objects and store in variable called student

    # figure out how to pass data stored in the above variable to template(view.html)
    # create a dictionary and pass it to template ('students': students)) a key which will be accessed by the html file
    return render(request, 'view.html', context={'navbar': 'view', 'data': students })
