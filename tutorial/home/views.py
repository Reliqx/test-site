from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from home.forms import RegistrationForm
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

