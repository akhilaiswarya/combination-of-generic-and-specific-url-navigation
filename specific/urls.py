from django.urls import path
from specific.views import *
app_name='specific'
urlpatterns = [

    path('cherry/',cherry,name='cherry'),
    path('akshay/',akshay,name='akshay'),

]