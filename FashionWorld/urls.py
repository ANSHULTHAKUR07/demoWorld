from django.urls import path
from .views import *
from .import views


urlpatterns = [
    # path('createcategory', CategoryView.as_view(),name = 'createCategory'),
    # path('createproduct',CreateProductView.as_view(),name = 'createProduct'),
    # path('product/<int:pk>',ProductListView.as_view(), name='productlist'),
    # path('product1/<int:pk>',ProductListView1.as_view(), name='productlist1'),
    # path('productdetailsp/<int:pk>',ShowProductDetails.as_view(), name='productdetails'),
    # path('allcategories', CategoryList.as_view( ),name = 'categorylist'),
    path('createcategory', CreateCategory.as_view(),name = 'createCategory'), 
    path('createproduct', CreateProduct.as_view(),name = 'createProduct'), 
    path('listcategories', ListCategory.as_view( ),name = 'categorylist'),
    path('updatecategory/<int:pk>', UpdateCategory.as_view(),name = 'updateCategory'),
    path('product/<int:pk>',productDetails.as_view(), name='productlist'),
    path('singleproductdetails1/<int:pk>',SingleProductDetails.as_view(), name='singleproductdetails'),
    path('deletecategory/<int:pk>',DeleteCategory.as_view(), name='deletecategory'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    # path('searchproduct/',views.searchproduct,name='searchproduct'),
    path('search', SearchResultsView.as_view(), name='search_results'),



    
]