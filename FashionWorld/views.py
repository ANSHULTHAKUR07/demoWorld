from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import DetailView, ListView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .mixins import GroupRequiredMixin
from django.views.defaults import permission_denied
from django.contrib.auth.decorators import login_required, permission_required
from cart.cart import Cart
from decimal import Decimal
from .util import *
from django.conf import settings
from django.contrib.sessions.models import Session
import json
from django.db.models import Q
from .permissions import CustomePermissionCheck

# from .forms import *

# Create your views here.
class CategoryView( View):
    def post(self, request, *args, **kwargs):
        cname = request.POST.get('cname')
        print("__________jkk",request.FILES)
        image = request.FILES['cimage']
        Category.objects.create(cname=cname, cimage=image)
        return render(request, 'fashionworld/create_category.html')
    
    def get(self, request, *args, **Kwargs):
        print("_________________________JPIJIJIJJI")
        return render(request,'fashionworld/create_category.html')
    
    
    

# class CreateProductView(View):
#     def get(self, request, *args, **kwargs):
#         categories = Category.objects.all()
#         return render(request, 'fashionworld/create_product.html', context={'categories':categories})
    
#     def post(self, request, *args, **kwargs):
#         pname = request.POST.get('pname')
#         pprice = request.POST.get('pprice')
#         pdesc = request.POST.get('pdesc')
#         pimage = request.FILES['pimage']
#         categoryid = request.POST.get('pcategory')
#         category = Category.objects.get(id=categoryid)
#         kwargs = {"pname":pname,"pprice":pprice,'pcat':category,'pdesc':pdesc,'pimage':pimage}
#         Product.objects.create(**kwargs)
#         return render(request, 'fashionworld/create_product.html')
    

# class CategoryList(View):

#     def get(self, request, *args, **kwargs):
#         cateorgies_list = Category.objects.all()
#         return render(request, 'fashionworld/categorylist.html', context={'categories':cateorgies_list})
    

# class ProductListView(View):
#     def get(self, request, *args, **kwargs):
#         category_id = kwargs.get('pk')
#         category = Category.objects.get(id=category_id)
#         category_products = Product.objects.filter(pcat=category)
#         print("product_list",category_products)
#         return render(request, 'fashionworld/productlist.html',context={'products':category_products})
    

    
# class ProductListView1(View):
#     def get(self, request, *args, **kwargs):
#         category_id = kwargs.get('pk')
#         category = Category.objects.get(id=category_id)
#         category_products = Product.objects.filter(pcat=category)
#         print("product_list",category_products)
#         return render(request, 'fashionworld/productlist1.html',context={'products':category_products})
    

# class ShowProductDetails(View):
#     def get(self, request, *args, **kwargs):
#         product_id = kwargs.get('pk')
#         product = Product.objects.get(id=product_id)
#         print(product.pname)
#         print(product.pprice)
#         print(product.pdesc)
#         print(product.pcat)
#         return render(request, 'fashionworld/productdetails.html',context={'products':product})

    
    

class CreateCategory(PermissionRequiredMixin, CreateView):
    permission_required = "user.show_profile"
    model = Category
    fields = ['cname','cimage']
    template_name = 'fashionworld/create_category.html'
    success_url = '/'

class CreateProduct(PermissionRequiredMixin, CreateView):
    permission_required = ["FashionWorld.add_product"]
    model = Product
    fields = '__all__'
    template_name = 'fashionworld/create_product.html'
    success_url = '/'


class ListCategory(PermissionRequiredMixin, ListView):
    permission_required = ["user.show_product"]
    model = Category
    fields = ['cname', 'cimage']
    template_name = 'fashionworld/categorylist.html'
    success_url = '/'


class productDetails(ListView):
    model = Product
    fields = ['name', 'image', 'pcat']
    paginate_by = 1
    template_name = 'fashionworld/SingleCategoryProductLists.html'
    print(object)
    success_url = '/'

    def get_queryset(self):
        category = Category.objects.get(id=self.kwargs.get('pk'))
        return Product.objects.filter(pcat=category)

    def get_context_data(self, **kwargs: Any):
        extra_data = super().get_context_data(**kwargs)
        extra_data['course_details']={'subject':'python'}
        # print("QRERWR_____________",extra_data['page_obj'].__dict__['paginator'].__dict__)
        return extra_data



class SingleProductDetails(DetailView):
    model = Product
    fields = ['name', 'price', 'pdesc', 'image']
    template_name = 'fashionworld/showproductdetails.html'
    success_url = '/'


class UpdateCategory(UpdateView):
    model = Category
    fields = ['cname','cimage']
    template_name = 'fashionworld/create_category.html'
    success_url = '/'


class DeleteCategory(DeleteView):
    model = Category
    template_name = 'fashionworld/create_category.html'
    success_url = '/'




@login_required(login_url="/user/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id) 
    cart.add(product=product)
    # print(request.user.id, "user id when add product")
    # request.session['user_id'] = request.user.id
    return redirect("cart_detail" )

@login_required(login_url="/user/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('cart_detail')

@login_required(login_url="/user/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('cart_detail')

@login_required(login_url="/user/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect('cart_detail')

@login_required(login_url="/user/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')

@login_required(login_url="/user/login")
def cart_detail(request):
    cart = Cart(request)

    if not request.session.get('cart'):
        user_id = str(request.user.id)
        try:
            cart = request.COOKIES[user_id]
            request.session['cart']=json.loads(cart)
        except KeyError:
            request.session['cart']={}
        
    print(request.COOKIES)
    total = totalprice(request)
    return render(request, 'fashionworld/cart.html', context={'total_price': total})



class SearchResultsView(ListView):
    print("search view method")
    model = Product
    template_name = 'home/homepage.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('search')
        print(query, "++++query set ")
        products=Product.objects.filter(Q(name__icontains=query))
        print(products, "all products")
        return products



