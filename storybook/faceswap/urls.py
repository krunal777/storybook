from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

#now import the views.py file into this code
from . import views
urlpatterns=[
  path('',views.homePage),
  path('success', views.success, name='success'),
  path('hotel_images', views.display_hotel_images, name = 'hotel_images'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)