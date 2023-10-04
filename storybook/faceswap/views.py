from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    return render(request,"index.html")

def index(request):
    return HttpResponse("Hello word")