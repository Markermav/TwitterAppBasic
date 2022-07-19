# from lib2to3.pgen2.tokenize import generate_tokens
# from tracemalloc import DomainFilter
# from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib import messages
# from requests import request
from django.contrib.auth import authenticate, login, logout
from authentication import validation
# from Authenticator import settings
# from django.core.mail import send_mail, EmailMessage

# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode
# from django.utils.http import urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from .tokens import generate_Token
# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
       # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        a = validation.validate_form(request, username, email, pass1, pass2)
        if a != 'error':
        # if User.objects.filter(username = username):
        #     messages.error(request, 'username already taken')
        #     return redirect('home')
        # if User.objects.filter(email=email).exists():
        #     messages.error(request, "Email Already Registered!!")
        #     return redirect('home')
        
        # if len(username)>20:
        #     messages.error(request, "Username must be under 20 charcters!!")
        #     return redirect('home')
        
        # if pass1 != pass2:
        #     messages.error(request, "Passwords didn't matched!!")
        #     return redirect('home')
        
        # if not username.isalnum():
        #     messages.error(request, "Username must be Alpha-Numeric!!")
        #     return redirect('home')
            
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.is_active = True

            
            myuser.save()

            messages.success(request, "Your account created successfuly, you can login now")

            # welcome email logic
            
            # subject = 'Hello , thanks for signing up on my website'
            # message = "Hello" + myuser.first_name + "\n" + "Please verify your account \n\n Thanks !"
            # from_email = settings.EMAIL_HOST_USER
            # to_list=[myuser.email]
            # send_mail(subject, message, from_email, to_list, fail_silently=False)

            # Email confirmation

            # current_site = get_current_site(request)
            # email_subject = 'Confirm your email for logging in successfuly'
            # message2 = render_to_string('emailconfirm.html', {
            #     'name' : myuser.first_name,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            #     'token': generate_Token.make_token(myuser)
            # })
            # email = EmailMessage(
            #     email_subject,
            #     message2,
            #     settings.EMAIL_HOST_USER,
            #     [myuser.email],
            # )
            # email.fail_silently =True
            # email.send()


            return redirect('home')
        else:
            return redirect('home')
    return render(request, "authentication/signup.html")    



def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname= user.first_name
            messages.success(request, "User successfully Logged in")
            return redirect('home1')   
            # return render(request, "authentication/index.html", {"fname":fname})   
        else:
            messages.error(request, "Bad Credentials") 
            return redirect('home')   
    return render(request, "authentication/signin.html")  



def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!") 
    return redirect('home')     



# def activate(request, uid64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uid64))  
#         myuser = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         myuser = None

#     if myuser is not None and generate_Token.check_token(myuser, token):
#         myuser.is_active = True
#         myuser.save()
#         login(request, myuser)
#         return redirect('home')

#     else:
#         return HttpResponse('Activation failed')         