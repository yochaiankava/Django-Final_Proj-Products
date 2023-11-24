from rest_framework import serializers
from .models import *



class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=True,read_only=True)
    class Meta:
        model = Product
        fields = '__all__' 
        # example of how to filter fields. remove line 7 __all__ and replace with line 9:
        # fields = ['name','price']
        
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

    

class CartItemSerializer(serializers.ModelSerializer):   
    product_name = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = '__all__'

    def get_product_name(self, obj):
        return obj.product.name       

class CartSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    cartitems = CartItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cart
        fields = '__all__'
    
    def get_customer_name(self, obj):
        return obj.customer.username   

class GiftCardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GiftCard
        fields = '__all__'
