from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from user.models import UserProfile


# Create your views here.


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        name = request.POST.get('name')
        birth_year = request.POST.get('birth_year')
        birth_month = request.POST.get('birth_month')
        birth_day = request.POST.get('birth_day')
        phone_number1 = request.POST.get('phone_number1')
        phone_number2 = request.POST.get('phone_number2')
        phone_number3 = request.POST.get('phone_number3')

        phone_number = f"{phone_number1}-{phone_number2}-{phone_number3}"
        birth_date = f"{birth_year}-{birth_month.zfill(2)}-{birth_day.zfill(2)}"
        if password != password_confirm:
            messages.error(request, "비밀번호가 일치하지 않습니다.")
            return render(request, 'user/signup.html')
        try:
            user = User.objects.create_user(username=username, password=password)
            UserProfile.objects.create(
                user=user,
                name=name,
                birth_date=birth_date,
                phone_number=phone_number

            )

            messages.success(request, "회원가입이 완료되었습니다.")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"회원가입 중 문제가 발생했습니다: {e}")
            return render(request, 'user/signup.html')

    return render(request, 'user/signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "아이디 또는 비밀번호가 올바르지 않습니다.")
            return redirect('login')

    return render(request, 'user/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')
