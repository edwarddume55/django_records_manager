from django.shortcuts import render,redirect

from .forms import UserCreationForm,LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


#homepage
def home(request):

    return render(request, 'base/index.html')

    
#register
def register(request):
    Form= UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if Form.is_valid():
            form.save()
            return redirect("login")

    context = {'form':Form}
    return render (request, 'base/register.html', context=context)

#login
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user =authenticate(request, username=username, password= password)

            if user is not None:
                auth.login(request, user)

                return redirect('dashboard')

    context ={'form': form}
    return render(request, 'base/login.html', context=context)


#user_logout
def user_logout(request):
    auth.logout(request)
    return redirect("login")


#dashboard
@login_required(login_url='login')
def dashboard(request):

    return render(request, 'base/dashboard.html')