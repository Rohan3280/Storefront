from django.urls import path
from . import views

#UrlConf
urlpattern =[
    path('playground/hello',views.say_hello)
]