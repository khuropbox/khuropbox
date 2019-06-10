from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from khuropbox import settings
from khuropbox import CognitoAuth
import hashlib

import django


def index(request):
    if request.user.is_authenticated:
        return render(request, "main.html")
    else:
        return render(request, "login.html")

def login(request):
    if request.user.is_authenticated:
        raise PermissionDenied
    else:
        if request.method == "POST":
            if not all(i in request.POST for i in ('username', 'password')):
                return render(request, "login.html", {
                    "message": "아이디와 비밀번호를 입력해 주세요"
                })

            un = request.POST['username']
            pw = request.POST['password']

            user = authenticate(username=un, password=pw)

            if user is not None:
                auth = django.contrib.auth.login(request, user)

                hashcode = hashlib.md5(request.POST['password'].encode('utf-8')).hexdigest()

                cog = CognitoAuth.Cognito()
                cog.sign_in_admin(username=un, password=hashcode)

                return redirect('/')
            else:
                return render(request, "login.html", {
                    "message": "아이디와 비밀번호를 확인해 주세요"
                })
        else:
            return render(request, "login.html")

def logout(request):
    if request.user.is_authenticated:
        django.contrib.auth.logout(request)

    return redirect("/")

def register(request):
    Cog = CognitoAuth.Cognito()
    if request.user.is_authenticated: raise PermissionDenied
    if request.method == "POST":
        require_keys = ('username', 'password', 'first_name', 'last_name', 'email')
        if all(i in request.POST for i in require_keys):
            if User.objects.filter(username=request.POST['username']).count():
                return render(request, 'register.html', {
                    "message": '이미 존재하는 아이디입니다.'
                })
            if User.objects.filter(email=request.POST['email']).count():
                return render(request, 'register.html', {
                    "message": '이미 존재하는 이메일입니다.'
                })

            userobj = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email']
            )

            hashcode = hashlib.md5(request.POST['password'].encode('utf-8')).hexdigest()

            Cog.sign_up(
                        username=request.POST['username'],
                        password=hashcode,
                        UserAttributes=[
                            {
                                'Name' : 'email',
                                'Value' : request.POST['email'],
                            },
                            {
                                'Name' : 'family_name',
                                'Value': request.POST['first_name'],
                            },
                            {
                                'Name' : 'given_name',
                                'Value': request.POST['last_name'],
                            },
                        ])

            Cog.confirm_sign_up(username=request.POST['username']);

            return redirect('/')
        else:
            return render(request, 'register.html', {
                "message": '모든 항목을 입력해주세요.'
            })
    else:
        return render(request, 'register.html')
