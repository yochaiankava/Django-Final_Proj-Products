from rest_framework import status
from django.shortcuts import render
from .models import *
from .serializers import *
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication




@api_view(['GET', 'POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def products(request):
    # print(request.headers)
    if request.method == 'GET':
        search = request.GET.get('search')
        maxprice = request.GET.get('maxprice')        
        category = request.GET.get('category')

        all_products = Product.objects.all()
        
        # search all product that name contains search parameter
        if search:
            all_products = all_products.filter(name__icontains=search)
        # search all product that price <= maxprice (price__lte=maxprice)
        if maxprice:
            all_products = all_products.filter(price__lte=maxprice)
        # Filter by category if 'category' parameter is provided    
        if category:  
            all_products = all_products.filter(category=category)    

        all_products_json = ProductSerializer(all_products, many=True).data
        return Response(all_products_json)
    elif request.method == 'POST':
        # this line creates a serializer object from json data
        serializer = ProductSerializer(data=request.data)
        # this line checkes validity of json data
        if serializer.is_valid():
            # the serializer.save - saves a new product object
            serializer.save()
            # returns the object that was created including id
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if not valid. return errors.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):    
    # get object from db by id
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        # create serializer from object
        serializer = ProductSerializer(product)
        # return json using serializer
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    elif request.method == 'DELETE':
        # product.is_active = False
        # product.save()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view()
# def categories(request):
#     search = request.GET.get('search')
#     all_categories = Category.objects.all()
#     if search:
#         all_categories = all_categories.filter(name__contains=search)
#     all_categories_json = CategorySerializer(all_categories, many=True).data
#     return Response(all_categories_json)

@api_view(['GET', 'POST'])
def categories(request):
    if request.method == 'GET':
        search = request.GET.get('search')
       
        all_categories = Category.objects.all()
        # search all product that name contains search parameter
        if search:
            all_categories = all_categories.filter(name__contains=search)        

        all_categories_json = CategorySerializer(all_categories, many=True).data
        return Response(all_categories_json)
    elif request.method == 'POST':
        # this line creates a serializer object from json data        
        serializer = CategorySerializer(data=request.data)
        # this line checkes validity of json data 
        if serializer.is_valid():
            # the serializer.save - saves a new product object
            serializer.save()
            # returns the object that was created including id
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if not valid. return errors.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, id):
    # get object from db by id
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        # create serializer from object
        serializer = CategorySerializer(category)
        # return json using serializer
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    elif request.method == 'DELETE':
        # product.is_active = False
        # product.save()
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def cart(request):
#     if request.method == 'GET':       

#         all_carts = Cart.objects.all()              

#         all_carts_json = CartSerializer(all_carts, many=True).data
       
#         return Response(all_carts_json)

#     elif request.method == 'POST':
#         # this line creates a serializer object from json data        
#         serializer = CartSerializer(data=request.data)
#         # this line checkes validity of json data 
#         if serializer.is_valid():
#             # the serializer.save - saves a new product object
#             serializer.save()
#             # returns the object that was created including id
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # if not valid. return errors.
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

@api_view(['GET', 'POST'])
def cart(request):
    if request.method == 'GET':
        # Get user ID from the request query parameters
        user_id = request.query_params.get('user_id')

        # Filter carts based on user ID if provided
        if user_id is not None:
            user_carts = Cart.objects.filter(customer=user_id)
        else:
            # If user ID is not provided, return all carts
            user_carts = Cart.objects.all()

        # Serialize the filtered carts
        user_carts_json = CartSerializer(user_carts, many=True).data

        return Response(user_carts_json)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cart_detail(request, id):
    # get object from db by id
    try:
        cart = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        # create serializer from object
        serializer = CartSerializer(cart)
        # return json using serializer
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    elif request.method == 'DELETE':
        # product.is_active = False
        # product.save()
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def cart_items(request):
    if request.method == 'GET':
        # Retrieve all cart items
        cart_items = CartItem.objects.all()
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new cart item
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cart_item_detail(request, pk):
    try:
        cart_item = CartItem.objects.get(pk=pk)
    except CartItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CartItemSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

@api_view()
def gift_cards(request):
    gift_cards = GiftCard.objects.all()
    serializer = GiftCardSerializer(gift_cards, many=True).data     
    return Response(serializer)
        