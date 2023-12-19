from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    phone_number = serializers.IntegerField(required=False, allow_null=True, write_only=True)
    address = serializers.CharField(required=False, allow_null=True, write_only=True)
    
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_phone_number(self, value):
        # Convert empty strings to None
        if value == '':
            return None

    def validate_address(self, value):
        # Convert empty strings to None
        if value == '':
            return None       
                       
        return value        

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        return user

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
    product_stock = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField()
    
    class Meta:
        model = CartItem
        fields = '__all__'

    def get_product_name(self, obj):
        return obj.product.name  
    def get_product_stock(self, obj):
        return obj.product.stock     
    def get_product_price(self, obj):
        return obj.product.price      
           

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
