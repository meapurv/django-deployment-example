from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'basic_app'



urlpatterns = [

    path('index/',views.index,name='index'),
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),

]
