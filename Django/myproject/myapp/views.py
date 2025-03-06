from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def index(request):
    name = "Shubham"
    return render(request, 'index.html', {'name': name}) #home page url is mapped to index.html

def about(request):
    return render(request, 'about.html') #about page url is mapped to about.html

def contact(request):
    return render(request, 'contact.html') #contact page url is mapped to contact.html

def counter(request):
    text = request.POST['text'] #get the text from the form
    words = len(text.split()) #number of words ißn the text
    char_count = len(text) #number of characters in the text
    return render(request, 'counter.html', {
        'text': text,
        'words': words,
        'char_count': char_count,

    }) #counter page url is mapped to counter.html

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        new_contact = Contact(name=name, email=email, subject=subject, message=message)
        new_contact.save()
        
        messages.success(request, f"Thanks {name} Your message has been sent successfully. We will get back to you soon.")
        return redirect('contact')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, f"Username {username} is already taken. Please try another username.")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, f"Email {email} is already taken. Please try another email.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
            
                messages.success(request, f"Thanks {username} Your account has been created successfully. Login to continue.")
                return redirect('login')
        else:
            messages.error(request, "Password and Confirm Password do not match. Please try again.")
            return redirect('register')

    return render(request, 'register.html') #register page url is mapped to register.html

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')
    
    return render(request, 'login.html') #login page url is mapped to login.html

def logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('/')

def months(request):
    months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    months_with_numbers = [{'name': month, 'number': i+1} for i, month in enumerate(months_list)]
    return render(request, 'months_list.html', {'months': months_with_numbers})

def month_detail(request, month_number):
    months_list = ['January', 'February', 'March', 'April', 'May', 'June', 
                  'July', 'August', 'September', 'October', 'November', 'December']
    
    # Check if the month number is valid (1-12)
    if 1 <= month_number <= 12:
        month_name = months_list[month_number-1]
        return render(request, 'month_detail.html', {
            'month_number': month_number,
            'month_name': month_name
        })
    else:
        # Handle invalid month number
        return HttpResponse("Invalid month number", status=404)
