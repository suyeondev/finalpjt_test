from django.shortcuts import render

# Create your views here.
def index(request):
    print('fromApp index~~')
    return render(request, 'front/index.html')