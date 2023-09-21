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
    path('profile_details/',UserProfile.as_view(),name='profile_details'),
    path('addbyfriend/<int:id>',AddFriends.as_view(),name='addbyfriend'),
    path('friendadd/<int:id>',FriendAdded.as_view(),name='friendadd'),
    path('showFriendDetails/<int:id>',ShowFriendList.as_view(),name='showFriendDetails'),
    path('showFriendprofile/<int:id>',ShowFriendProfile.as_view(),name='showFriendprofile'),
    path('showFriendfriendslist/<int:id>',ShowFriendsFriendList.as_view(),name='showFriendfriendslist'),
   
    
   

]