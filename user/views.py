from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import ShoppingUser
from django.contrib.auth import login as auth_login, authenticate, logout,get_user_model
from .forms import UserForm
from cart.cart import Cart
import copy
from django.conf import settings
from django.contrib.sessions.models import Session
from django.shortcuts import HttpResponse
from.models import *
import random
from django.core.mail import send_mail
from django.views import View
from datetime import datetime
ShoppingUser = get_user_model()
import re
from django.utils import timezone
import time
from .util import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q



# # Create your views here.
import json
# def signup(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         cpassword = request.POST.get('cpassword')
#         phone = request.POST.get('phone')
#         firstname = request.POST.get('firstName')
#         lastname = request.POST.get('lastName')
#         gender = request.POST.get('gender')
#         state = request.POST.get('state')
#         print(email, password, cpassword, phone, firstname, lastname, gender, state)

#         conditions = [
#             len(email)==0 or email.isspace(),
#             len(password)==0 or password.isspace(),
#             len(cpassword)==0 or cpassword.isspace(),
#             len(phone)==0 or phone.isspace(),
#             len(firstname)== 0 or firstname.isspace(),
#             len(lastname)==0 or lastname.isspace(),
#             len(gender)==0 or gender.isspace(),
#             len(state)==0 or state.isspace()
#         ]
#         if not any(conditions):
#             if len(password)<5 and len(password)>15:
#                 messages.error(request, "Password denied: must be between 5 and 15 characters long.")
#             elif re.search('[0-9]',password) is None:
#                 messages.error(request, "Password denied: must contain a number between 0 and 9")
#             elif re.search('[A-Z]',password) is None:
#                 messages.error(request, "Password denied: must contain a capital letter.")
#             elif re.search('[a-z]',password) is None:
#                 messages.error(request, "Password denied: must contain a lowercase letter.")
#             # elif re.search('[!, @, #, $, %, &, (, ), -, _, [, ], {, }, ;, :, ", ., /, <, >, ?]', password) is None:
#             #     messages.error(request, "Password denied: must contain a special character")    
#             else:
#                 if password == cpassword:
#                     if ShoppingUser.objects.filter(email=email).exists():
#                         messages.success(request, "User with this email already exists.")
#                         return redirect('/user/register')
#                     user = ShoppingUser.objects.create_user(email=email, password=password, phone_number=phone, first_name=firstname, last_name = lastname, gender = gender, state = state)
#                     if user:
#                         messages.success(request, "you are successfully registerd")
#                         return redirect('/')

#                 else:
#                     messages.error(request, "password can not be matched")
#         else:
#             messages.error(request, 'all fields are required')

#     return render(request, 'user/signup.html')

def login(request):
    if request.method == 'POST':
        email1 = request.POST['email']
        password2 = request.POST['password']
        
        conditions = [
            len(email1)==0 or email1.isspace(),
            len(password2)==0 or password2.isspace()
        ]
        

        if not any(conditions):
            user = authenticate(request, email=email1,password=password2)
            if user is not None:
                auth_login(request, user)
                print("_____REQUEST.POST__",request.POST)
                if "next" in request.POST:
                    next_url = request.POST.get('next')
                    return redirect(next_url)
            
                return redirect('/')
            else:
                messages.error(request, "Invalid credentials")
                return redirect('/user/login')
            
        else:
            messages.error(request, "all fields are required")

    return render(request, 'user/login.html')

def logout_user(request):

    cart = request.session.get('cart')
    user_id = request.user.id
    logout(request)  
    response = redirect('/user/login')
    response.set_cookie(str(user_id), json.dumps(cart), max_age=300)
    return response

def signup(request):
    userform = UserForm()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            user = userform.save(commit=True)
            print(user.id, "+++++++")
            otp = str(random.randint(10000,100000))
            print(otp)
            userotp = Otpgenrator.objects.create(userid = user, otp=otp)
            userotp.created_at = timezone.now()
            userotp.save()
            print(userotp.id, "userotp id ++++++")
            print(userotp.userid, "userid from user table")
            print(userotp.otp, "its generated otp")
            print(userotp.created_at, "datetime")

            request.session['user_id'] = userotp.userid.id
            request.session['resend_otp'] = userotp.otp

            verification_link = f"http://127.0.0.1:8000/user/verify/?email={user.email}&otp={otp}"
            try:
                send_mail(
                    subject ="OTP for registration",
                    message = f'your Verification link is: {otp}',
                    from_email="justthink01234@gmail.com",
                    recipient_list=['anshulthakar07@gmail.com'],
                    fail_silently=False
                )
            
            except Exception as e:
                print(e)
                messages.error(request, "failed to send verfiction email ")
            else:
                messages.success(request, "you have singed up successfully please check your email id and verify your account  ")
                print("else part of return redirect +++")
                request.session['email'] = user.email
                return redirect("verify/")
              
    return render(request, 'user/signup.html',context={'form':userform})


class VerifyOtp(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'user/verify_otp.html')
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            session_otp = False
            user_id = request.session.get('user_id')
            email = request.session.get('email')
            otp = request.POST.get('otp')
            print(user_id, "-----")
            current_time = timezone.now()
            current_time = current_time
            print(current_time, "current time zone")
            user = None
            try:
                user = Otpgenrator.objects.get(userid = user_id)
                created_at = user.created_at
            except Otpgenrator.DoesNotExist:
                session_otp = True
                otp = request.session["otp"]
                created_att = request.session["current_time"]
                print(created_att, "get session date in datetime")
                print(type(created_att), "get session date")
                created_at = datetime.strptime(created_att, '%Y-%m-%dT%H:%M:%S')
                created_at = timezone.make_aware(created_at, timezone=timezone.utc)
            print(type(created_at), "user created at in post method --------")
            print(created_at, "date in object from")
            time_difference = current_time - created_at
            print(time_difference, "time difference -----------")
            if time_difference.total_seconds() > 600:
                if user:
                    user.delete()
                messages.error(request, "OTP has expired. click on resend button to resend new otp. ")
                return render(request, "user/verify_otp.html") 

            else:
                if session_otp:
                    otp = request.session.get('otp')
                    email = request.session.get("email")
                    get_otp_from_session(request, otp, user_id)
                    return render(request, "user/verify_otp.html")
                else:
                    get_otp_from_db(request, otp, email)
                    return render(request, "user/verify_otp.html")
            
                             
def resendOtp(request):
    if request.method == 'GET':
        resend_otp = request.session.get("resend_otp")
        current_time = timezone.now()
        dateinv = datetime.strftime(current_time, '%Y-%m-%dT%H:%M:%S')
        print(type(dateinv), "datein regenrate otp")
        request.session['current_time'] = dateinv
        print(resend_otp, "resend otp to the user")
        try:
            send_mail(
                subject ="OTP for registration",
                message = f'your Verification link is: {resend_otp}',
                from_email="justthink01234@gmail.com",
                recipient_list=['anshulthakar07@gmail.com'],
                fail_silently=False
            )
        
        except Exception as e:
            print(e)
            messages.error(request, "failed to send verfiction email ")
        else:
            messages.success(request, "you have singed up successfully please check your email id and verify your account  ")
            print("else part of return redirect +++")
            return redirect("/user/verify")
    return render(request, "user/verify_otp.html")


class UserProfile(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            profile = request.user.profile
            print(profile, "=========> user profile details")
            return render(request, "user/profile.html", {'profile': profile})
        
    def post(self, request, *args, **kwargs):
        print( "user first name in update data")
        u_id = request.POST.get('userid')
        p_id = request.POST.get('profileid')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        state = request.POST.get('state')

        user = ShoppingUser.objects.get(pk=u_id)
        if user:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.phone_number = phone_number
            user.gender = gender
            user.state = state
            user.save()

        if 'image' in request.FILES:
            image = request.FILES['image']
            print(image, "wklehfowrgbejgjvwbjlk======.......=====")
            profileid = Profile.objects.get(pk=p_id) 
            profileid.id = p_id
            profileid.user_id = u_id
            profileid.image = image
            profileid.save()
            print("profile updatred succesfully")
        
        print(u_id,p_id,first_name,last_name,email,password,phone_number,gender,state)
        return redirect("/user/profile_details")
    
class AddFriends(View):
    def get(self, request, *args, **kwargs):
        userid = kwargs.get('id')
        print(userid, "it is in friend list view ++++++")
        user = ShoppingUser.objects.all()
        return render(request, "user/friendlist.html", context={'user':user, 'user_id':userid})
    

class FriendAdded(View):
    def get(self, request, *args, **kwargs):
            userid = request.GET.get('userid')
            main_user = ShoppingUser.objects.get(id = userid)
            print(userid,"userid +++++++++++88888888888888888888")
            print(request.GET)
            user_id = kwargs.get('id')
            print(user_id, "friend id +++++++++++++++++++++++++++++")
            single_user = ShoppingUser.objects.get(id = user_id)
            print(single_user, "singleuser +++++++++++++++++++++++++++++")
            main_user.friends.add(single_user)
        
            return redirect("/user/profile_details")
        

    def post(self, request, *args, **kwargs):
        return render(request, "user/login.html")    
    
    
class ShowFriendList(View):
    def get(self, request, *args, **kwargs):
        print("show friend list page ++++++++__________")
        user_id = kwargs.get('id')
        # all_friends = ShoppingUser.objects.get(id = user_id)
        # total_friends = all_friends.friends.filter(id__gt=1)
        # profile_user = Profile.objects.get(user_id=all_friends)
        result = friends_profile_list_of_friends(request, user_id)
        total_friends = result['friends']
        profile_user = result['profile']

        return render(request, "user/profile.html", context={"friends": total_friends, 'profile':profile_user})

class ShowFriendProfile(View):
    def get(self, request, *args, **kwargs):
        print("show frireefknevncejnvcjoenfvnvksnvknvo9874548469====")
        friend_id = kwargs.get('id')
        # friend_profile = ShoppingUser.objects.get(id = friend_id)
        # profileimage = Profile.objects.get(user_id = friend_id)
        result = result = friends_profile_list_of_friends(request, friend_id)
        friend_profile = result['userprofile']
        profileimage = result['profile']
        print(friend_profile, "user profile=-=-=-=-=----")
        return render(request, "user/friendprofile.html", context={"userprofile":friend_profile, 'profile':profileimage})
    

class ShowFriendsFriendList(View):
    permission_required = "user.can_add_data"
    def get(self, request, *args, **kwargs):
        print("show all friends list 1236547891236547891236547899")
        user_id = kwargs.get('id')
        # all_friends = ShoppingUser.objects.get(id = user_id)
        # total_friends = all_friends.friends.filter(id__gt=1)
        # profileimage = Profile.objects.get(user_id = user_id)
      
        result = friends_profile_list_of_friends(request, user_id)
        total_friends = result['friends']
        profileimage = result['profile']
        all_friends = result['userprofile']
        print("all friends --------------------------------------------------")
        return render(request, "user/friendprofile.html", context={"friends":total_friends, "profile":profileimage, "userprofile":all_friends})
    

class SearchFriend(ListView):
    model = ShoppingUser
    fields = "friends"
    template_name = "user/profile.html"
    context_object_name = "userfriend"

    def get_queryset(self):
        query = self.request.GET.get('search')
        print(query, "++++query set ")
        friends=ShoppingUser.objects.filter(Q(friends__icontains=query))
        print(friends, "all friends")
        return friends
    

   
        
    




                

 








