from django.urls import path
from frontapp import views

urlpatterns = [
    path('main/',views.index),

]
