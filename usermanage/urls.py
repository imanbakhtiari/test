from django.urls import path, include
from django.conf import settings
from . import views 
import debug_toolbar
  

urlpatterns= [
    path('advice/',views.advice),
    path('joke',views.dad_joke),
    path('spacex',views.next_spacex_launch),
    path('cat',views.random_cat_image),
]
