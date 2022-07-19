from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect


def validate_form(request, username, email, pass1, pass2):
    a = ''
    if User.objects.filter(username = username):
            messages.error(request, 'username already taken')
            a = 'error'

    if User.objects.filter(email= email).exists():
            messages.error(request, "Email Already Registered!!") 
            a = 'error'
   
    if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            a = 'error'
            
    if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            a = 'error'

    if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            a = 'error'
    return a