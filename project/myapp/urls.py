from django.urls import path
from django.urls import re_path

from .views import *


urlpatterns = [
    path('AdminRegister/', AdminRegisterView.as_view(), name='AdminRegister'),
    path('AdminRegister/<int:pk>', AdminRegisterView.as_view(), name='AdminRegister'),
    path('AdminLogin/', AdminLoginView.as_view(), name='AdminLogin'),

    path('UserRegister/', UserRegisterView.as_view(), name='UserRegister'),
    path('UserRegister/<int:pk>', UserRegisterView.as_view(), name='UserRegister'),
    path('UserLogin/', UserLoginView.as_view(), name='UserLogin'),

    path('UserRegister/', UserRegisterView.as_view(), name='UserRegister'),
    path('UserRegister/<int:pk>', UserRegisterView.as_view(), name='UserRegister'),
    path('UserLogin/', UserLoginView.as_view(), name='UserLogin'),


    path('Book/', BookView.as_view(), name='Book'),
    path('Book/<int:pk>', BookView.as_view(), name='Book'),
    
    path('BookRecord/', BookRecordView.as_view(), name='BookRecord'),
    path('BookRecord/<int:pk>', BookRecordView.as_view(), name='BookRecord'),

    re_path(r'^.*$', index)
]