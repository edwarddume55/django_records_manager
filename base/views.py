from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    return render(request, 'base/index.html')

    # return HttpResponse('Hello world!')
