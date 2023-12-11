from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import cart_items_count
# from .views import get_cart_total

urlpatterns = [
    
    
    path('product/', views.products, name="products"), 
    path('product/<id>', views.product_detail, name="product_detail"), 
    path('category/', views.categories, name="categories"),    
    path('category/<id>', views.category_detail, name="category_detail"), 
    path('cart/', views.cart, name="cart"),    
    path('cart/<id>', views.cart_detail, name="cart_detail"), 
    path('cartitem/', views.cart_items, name="cart_items"),  
    path('cartitem/<int:pk>/', views.cart_item_detail, name="cart_item_detail"),  
    path('gift_cards/', views.gift_cards, name="gift_cards"), 
    path('cartitems/count/<int:user_id>/', cart_items_count, name='cart_items_count'),
    # path('cart/<int:cart_id>/total/', get_cart_total, name='get_cart_total'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)