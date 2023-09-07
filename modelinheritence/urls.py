from django.urls import path
from .views import *
from . import views
urlpatterns = [
    # path('index',views.indexpage,name='index')
    path('index', Indexpage.as_view(),name = 'index'),
    path('deleteuser/<int:pk>',DeleteUser.as_view(), name='deleteuser'),
    path('updateuser/<int:pk>',UpdateUser.as_view(), name='updateuser'),
    path('studentattendence',StudentAttendenceView.as_view(), name='studentattendence'),
    path('personproxy',PersonProxyView.as_view(), name='personproxy')

]