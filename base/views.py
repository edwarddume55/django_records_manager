from django.shortcuts import render,redirect

from .forms import registerForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .models import Record

#homepage
def home(request):

    return render(request, 'base/index.html')

    
#register
def register(request):
    form= registerForm()

    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
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

    my_records = Record.objects.all()
    context = {'records': my_records}

    return render(request, 'base/dashboard.html', context=context)


#add a record
@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'base/create_record.html', context=context)


#update a record
@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context= {'form': form}
    return render(request, 'base/update_record.html', context=context)



#view a single record
@login_required(login_url='login')
def record(request, pk):
    all_records = Record.objects.get(id=pk)
    context={'record': all_records}
    return render (request, 'base/view_record.html', context=context)


#delete a record
@login_required(login_url='login')
def delete_record(request, pk):
    record= Record.objects.get(id=pk)
    record.delete()
    return redirect('dashboard')