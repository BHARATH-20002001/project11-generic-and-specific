from django.urls import path
from specific.views import *
app_name='specific'


urlpatterns=[
    path('spec1/',spec1,name='spec1'),
    path('spec2/',spec2,name='spec2'),

]