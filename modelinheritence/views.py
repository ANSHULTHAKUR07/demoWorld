from django.shortcuts import render
from modelinheritence.models import *
from django.views import View
from django.db.models import Q
from datetime import datetime
from django.utils import timezone

# Create your views here.

# def indexpage(request):
#     """
#     This is used to save the user into the database 
#     Get all the attributes of custom form and save user details into  the database using create method
#     """
#     if request.method == 'POST':
#         user_name = request.POST.get("username")
#         user_class = request.POST.get("userclass")
#         user_age = request.POST.get("userage")
#         user_phone = request.POST.get("phone")
#         user_rollno = request.POST.get("rollno")

#         Student.objects.create(user_name=user_name,  class_name=user_class, user_age = user_age, user_phone=user_phone, roll_number=user_rollno)
#         print("successfully register")
#     return render(request, "modelinheritence/index.html")

class Indexpage(View):
    """
    it is used to save user by inheriting View class in this i am using custom form 
    Get all the attribute of this form and save these attribute with create()
    """ 
    def get(self, request, *args, **kwargs):
        student = Student.objects.all()
        age_start = 0
        age_middle = 50
        less_fifty=None
        datelist = None
        age_last = request.GET.get("flexRadioDefault")
        age = request.GET.get("age")
        userclass = request.GET.get("userclass")
        todate = request.GET.get("todate")
        fromdate = request.GET.get("fromdate")
        monthvalue = request.GET.get("monthvalue")
        # print(fromdate)
        # print(type(todate))
        # print(age_last)
        # print(age)
        # print(userclass)
        if age_last is not None:
            if age_last=="50":
                less_fifty = Student.objects.filter(user_age__range=(age_start,age_last)).values()
                print(less_fifty)
            else:
                less_fifty = Student.objects.filter(user_age__range=(age_middle, age_last)).values()
                print(less_fifty)
        elif age and userclass is not None:
            print("+++++++++++++++++++++++++++++",age)
            print("---------------------------------------", userclass)
            # less_fifty = Student.objects.filter(user_age=age, class_name=userclass).values()
            less_fifty = Student.objects.filter(Q(user_age=age) & Q(class_name=userclass))
            print(less_fifty)

        elif monthvalue is not None:
            print(monthvalue)
            less_fifty = Student.objects.filter(created_at__month=monthvalue)
            print(less_fifty)
            
                

        elif todate and fromdate is not None:
            todate_obj = datetime.strptime(todate, '%Y-%m-%dT%H:%M')
            fromdate_obj = datetime.strptime(fromdate, '%Y-%m-%dT%H:%M')
            print(type(todate_obj))
            print(fromdate_obj)
            less_fifty = Student.objects.filter(created_at__gte=todate_obj, created_at__lte=fromdate_obj)
            print(less_fifty)
            

        else:
            if userclass is not None:
                # less_fifty = Student.objects.filter(class_name=userclass).values() | Student.objects.filter(class_name="Third").values()
                less_fifty = Student.objects.filter(Q(class_name=userclass) & Q(id__in=[1,5]))
                print(less_fifty)

        return render(request, "modelinheritence/index.html", {'st':student, 'filterstudents':less_fifty })
    
    def post(self, request, *args, **kwargs):
        user_name = request.POST.get("username")
        user_class = request.POST.get("userclass")
        user_age = request.POST.get("userage")
        user_phone = request.POST.get("phone")
        user_rollno = request.POST.get("rollno")

        kwargs = {"user_name":user_name, "class_name":user_class, "user_age":user_age, "user_phone":user_phone, "roll_number":user_rollno}
        Student.objects.create(**kwargs)
        print("successfully register")
        
        return render(request, "modelinheritence/index.html")
    
class StudentAttendenceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "modelinheritence/student.html")
    
    def post(self, request, *args, **kwargs):
        user_name = request.POST.get("username")
        user_class = request.POST.get("userclass")
        user_age = request.POST.get("userage")
        user_phone = request.POST.get("phone")
        user_rollno = request.POST.get("rollno")
        month = request.POST.get("month")
        present_days = request.POST.get("present")
        print( user_name, user_class,  user_age, user_phone,  user_rollno, month, present_days )
        kwargs = {"user_name":user_name, "class_name":user_class, "user_age":user_age, "user_phone":user_phone, "roll_number":user_rollno, "month":month, "present_days":present_days}
        StudentAttendance.objects.create(**kwargs)
        
        print("succesfully added attendence")

        return render(request, "modelinheritence/index.html")



class DeleteUser(View):
    def get(self, request, *args, **kwargs):
        userid = kwargs.get('pk')
        print(userid)
        deleteUser = Student.objects.get(id = userid)
        deleteUser.delete()
        print("user deleted succesfully deleted")

        return render(request, "modelinheritence/index.html")

   
class UpdateUser(View):
    def get(self, request, *args, **kwargs):
        userid = kwargs.get('pk')
        print(userid)
        user_obj = Student.objects.filter(id = userid)
        print(user_obj)
        context = {'user':user_obj}
        return render(request, "modelinheritence/update.html", context)
    
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = Student.objects.get(id = user_id)
        user.user_name = request.POST.get("username")
        user.class_name = request.POST.get("userclass")
        user.user_age = request.POST.get("userage")
        user.user_phone = request.POST.get("phone")
        user.roll_number = request.POST.get("rollno")
        user.save()
        print("user updated succesfully")
        return render(request, "modelinheritence/index.html")
    

class PersonProxyView(View):
     def get(self, request, *args, **kwargs):
        return render(request, "modelinheritence/personproxy.html")
     
     def post(self, request, *args, **kwargs):
         print("helloo")
         first_name = request.POST.get("firstname")
         last_name = request.POST.get("lastname")
         image = request.FILES['image']
         video = request.POST.get("urlvalues")
         type= request.POST.get("type")
         print(first_name, last_name, image, video, type)

         if type=="image":
            kwargs = {"first_name":first_name, "last_name":last_name, "image":image}
            PersonProxy.objects.create(**kwargs)
         else:
             kwargs = {"first_name":first_name, "last_name":last_name, "video":video, "type":type}
             PersonVideoProxy.objects.create(**kwargs)


# class PersonProxyList(View):
#          def get(self, request, *args, **kwargs):
#             personlist = PersonProxy.objects.all()
#             type = request.GET.get('type')
#             fn = request.GET.get('first_name')
#             personlist = PersonProxy.objects.filter(Q(type=type) | Q())

        
             
             
         
         return render(request, "modelinheritence/personproxy.html",)

