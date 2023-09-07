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
    