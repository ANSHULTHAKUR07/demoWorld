from django.shortcuts import render
from .models import ContactData
from django.contrib import messages
from FashionWorld.models import *
from user.models import *
from django.contrib.auth.decorators import permission_required, login_required
from django.core.exceptions import PermissionDenied
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger

# Create your views here.

def homeview(request):
    # request.session["name"] = "anshul"
    # request.session.set_expiry(10)
    # a = request.session.get("usercession")
    # print(a, "++++++++++")
    categories = Category.objects.all()
    products = Product.objects.all()

    # page = request.GET.get('page', 1)
    # paginator = Paginator(products, 2)

    # try:
    #     product = paginator.page(page)
    # except PageNotAnInteger:
    #     products = paginator.page(1)
    # except EmptyPage:
    #     products = paginator.page(paginator.num_pages)

    # return render (request, 'home/homepage.html', {'cats':categories,'product':products})
   
    return render(request, 'home/homepage.html',context={'cats':categories,'products':products})


@permission_required('home.add_contactdata', raise_exception=True)
def contactus(request):
        # ct = ContentType.objects.get_for_model(ContactData)
        # permission = Permission.objects.filter(codename='can_check_new_permission',content_type = ct).first()
        # permission = Permission.objects.create(codename='can_check_new_permission',content_type=ct, name='User can check for new permissions.')
        # request.user.user_permissions.add(permission)
        if request.method == 'POST':
            email = request.POST.get('emailid')
            message = request.POST.get('message')
            contactno = request.POST.get('phone')
            conditions = [
                len(email)==0 or email.isspace(),
                len(message)==0 or message.isspace(),
            ]
            if not any(conditions):
                if not contactno.isdigit():
                    messages.error(request, "only digits allowed in phone numnber")
                elif len(contactno)<10:
                    messages.error(request, "phone number should contain 10 digits")
                else:
                    ContactData.objects.create(email=email,message=message,phone_number=contactno)
                    messages.success(request, "Your form has been submitted.")
            else:
                messages.error(request, "all fields are required")
        return render(request, 'home/contactus.html')

@permission_required("user.show_profile", raise_exception= True)
def aboutus(request):
    return render(request, 'home/aboutus.html')
