from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .forms import HotelForm
from .models import Hotel

# Create your views here.
# def homePage(request):
#     return render(request,"index.html")

def homePage(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('/hotel_images')
    else:
        form = HotelForm()
      
    return render(request, 'index.html', {'form': form})
   
def success(request):
    return HttpResponse('successfully uploaded')


def display_hotel_images(request):
 
    if request.method == 'GET':
        # getting all the objects of hotel.
        Hotels = Hotel.objects.all()
        return render(request, 'display_hotel_images.html',{'hotel_images': Hotels}) 