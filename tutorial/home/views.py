from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from home.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def home(request):
    title = "Applewood Centre for Adult Learning"
    slogan = "Life Long Learning for People with Special Needs"

    args = {'title': title, 'slogan': slogan}
    return render(request, 'home/home.html', args)

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')

    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'home/register.html', args)


def profile(request):
    args = {'user': request.user}
    return render(request, 'home/profile.html',args)

def edit_profile(request):
    if request.method =="POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/home/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'home/edit_profile.html', args)

