from django.urls import path,include
from . import views

urlpatterns = [
    path('inshort-api/<str:category>/',views.inshort_api,name='inshort-api'),
]