from django.urls import path, include
from django.conf import settings
from . import views 
import debug_toolbar
  

urlpatterns= [
    path('hello/',views.hello),
]
