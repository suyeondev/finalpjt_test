from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print('portfolio page index~~')
    return render(request, 'portfolio/dashboard.html')
