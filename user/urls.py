from django.urls import path
from . import views
from .views import *

app_name='user'
urlpatterns = [
    path('register',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('verify/',VerifyOtp.as_view(), name='verify'),
    path('resendotp',views.resendOtp,name='resendotp'),
    
   

]