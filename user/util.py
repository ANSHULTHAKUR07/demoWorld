from.models import *
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.sessions.models import Session
from django.shortcuts import HttpResponse


def get_otp_from_db(request, otp, email):
    print(otp, "last")
    print(email, "last")
    try:
        user_otp = Otpgenrator.objects.get(userid__email=email, otp=otp)
        user_otp.delete() 
        messages.success(request, "OTP verified successfully!")
        return render(request, 'user/login.html')
    except Otpgenrator.DoesNotExist as e:
        print(e)
        messages.error(request, "Invalid OTP. Please try again.")
        return render(request, 'user/verify_otp.html')
    

def get_otp_from_session(request, otp, user_id):
    try:
        print(user_id, "userid")
        print(otp, "otp")
        user = Otpgenrator.objects.get(userid = user_id)
        print(user.userid, "user from database")
        print(user.otp, "otp from database")
        if user_id == user.userid and otp == user.otp:
            messages.success(request, "OTP verified successfully!")
            return render(request, 'user/login.html')
        
    except Otpgenrator.DoesNotExist as e:
        print(e)
        messages.error(request, "Invalid OTP. Please try again.")
        return render(request, 'user/verify_otp.html')
    

def friends_profile_list_of_friends(request, user_id):
    print(user_id, "is in function bro++++++++++++++++++++++++++++++++++++++++")
    try:
        all_friends = ShoppingUser.objects.get(id = user_id)
        print(all_friends, "12365478978965413anshul")
        total_friends = all_friends.friends.filter(id__gt=1)
        profileimage = Profile.objects.get(user_id = all_friends)
        all = {"friends":total_friends, "profile":profileimage, "userprofile":all_friends}

    except ShoppingUser.DoesNotExist as e :
        print(e)
        return render(request, "user/profile.html" )
    
    return all
    