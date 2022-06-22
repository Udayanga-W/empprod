from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
     path('',views.home),
     path('about/',views.about),
     path('leaves/',views.leaves),
     path('users/',views.users)

]
