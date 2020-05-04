from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from newapp.forms import UserInfo, UserProfileInfo
# Create your views here.
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


def index(request):
    return render(request, 'new_app/index.html')


def base(request):
    return render(request, 'new_app/base.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserInfo(data=request.POST)
        profile_form = UserProfileInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserInfo()
        profile_form = UserProfileInfo()

    return render(request, 'new_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


@login_required
def special_page(request):
    return HttpResponse("You have logged in succesfully")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('base'))


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('base'))
            else:
                print("Account not active")
        else:
            print("User not authencicated maliously")
            print(username, password)
            return HttpResponse("invalid request")
    else:
        return render(request, 'new_app/login.html')
