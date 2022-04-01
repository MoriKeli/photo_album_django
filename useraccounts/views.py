from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from datetime import datetime

from useraccounts.models import *


def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        user_password = request.POST['password']
        
        user = auth.authenticate(username=username, password=user_password)

        if user is not None:
            auth.login(request, user)

            current_date = datetime.today()
            current_hour = current_date.hour

            if current_hour >= 4 and current_hour <=12:
                messages.info(request, 'Good morning, {}'.format(username))
            elif current_hour == 12:
                messages.info(request, 'Good afternoon, {}'.format(username))
            else:
                messages.info(request, 'Good evening, {}'.format(username))
            return redirect('user_homepage')
        
        else:
            if user_password != auth.authenticate(password=user_password) and User.objects.filter(username=username).exists():
                messages.error(request, 'Incorrect password! Please try again.')
            else:
                messages.error(request, 'Invalid Credentials. Create an account.')
            return redirect('/')
    else:
        return render(request, 'login.html')

def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        gender = request.POST['gender']
        user_dob = request.POST['dob']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['c_password']

        if len(username)>30:
            messages.warning(request, 'Username provided too long!')
            return redirect('user_regist')
        elif (str(password).isalpha() and str(confirm_password).isalpha()) or (str(password).isnumeric() and str(confirm_password).isnumeric()):
            messages.error(request, 'Password(s) must contain atleast symbols: @$_?, atleast one letter and one digit.')
            return redirect('user_regist')
        elif len(password)<8:
            if len(confirm_password)<8:
                messages.error(request, 'Password(s) too short.')
            return redirect('user_regist')
        elif password != confirm_password:
            messages.error(request, 'Passwords not matching!')
            return redirect('user_regist')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username used to register another account. You can include either middle name or surname, or both in your username')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email address used to register another account.')
            return redirect('user_regist')
        else:
            auth_user_reg = User.objects.create_user(username=username, email=email, password=confirm_password)
            auth_user_reg.save()

            current_date = datetime.today()
            dob = datetime.strptime(user_dob, '%Y-%m-%d')
            age = current_date - dob

            save_user_details = Users.objects.create(name=username, gender=gender, phone_no=phone, date_of_birth=user_dob, age=int(age.days/365.25))
            save_user_details.save()

            messages.success(request, 'User {} registered successfully!'.format(username))
            return redirect('/')

    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Goodbyeeee... Thanks for using the website. See you soon.')
    return redirect('/')
