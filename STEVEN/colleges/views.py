from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm

from . import models
from . import admin
from . import email_info

# Create your views here.

def index(request):
    return render(request, 'colleges/index.html')

def login(request):
    return render(request, 'colleges/login.html')

def home(request):
    return render(request, 'colleges/home.html')

def students(request):
    return render(request, 'colleges/students.html')

# Automatic Email function triggered by save_model() overwrite
def mail(request):
    def getBody():
        text = """
        Thank you so much for registering %s to STEVEN - The Interntional Student Mentor.
        We really appreciate you believing in our work. \n\n
        You purchased %d slots for your international students. \n
        Please follow this link to validate your school:
        <Validationlink >\n\n
        And share this link with the students you wish to register:
        http://localhost:8000/registration/ \n\n
        We are always open to hearing your ideas and feedback on how we can improve!

        Feel free to reach out!
        - Samuel Padilla, CEO of STEVEN
        """ % (email_info.school, email_info.slots)
        return text
    
    Subject = 'Confirm your registration to StevenMentor'
    Body = getBody()
    from_email = 'steven@stevenmentor.com'
    to_email = email_info.recepient
    print (to_email)

    send_mail(Subject,
    Body,
    from_email,
    to_email,
    fail_silently=False)    
    return render(request, 'colleges/mail.html')


#Form handling
def registration(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            nationality = form.cleaned_data['nationality']
            major = form.cleaned_data['major']
            language = form.cleaned_data['language']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            New_Student = models.Student.objects.create(Name = name, User_Email = email, Nationality = nationality, Major = major, Language = language, Age = age)

            #CreateUser
            user = User.objects.create_user(
                name,
                email,
                password,
            )
            user.save()
            return render(request, 'colleges/index.html')

    form = RegistrationForm
    return render(request, 'colleges/registration.html', {'form':form})