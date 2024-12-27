from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Customer, Collection, Review, Cart, CartItem, Order, OrderItem
from .serializers import CustomerSerializer,ProductSerializer, CollectionSerializer, ReviewSerializer, CartSerializer, CartItemSerializer, CartItemAddSerializer, CartItemUpdateSerializer, OrderSerializer, OrderItemSerializer, OrderCreateSerializer, OrderUpdateSerializer
from .filters import ProductFilter
from .permissions import IsAdminOrReadOnly


class ProductViewSet(ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields=['collection_id']
    filterset_class=ProductFilter
    permission_classes=[IsAdminOrReadOnly]
    #search fields:
    search_fields=['title', 'description']
    ordering_fields=['price', 'last_update']
    # pagination_class=PageNumberPagination #also set the page size in rest_framework settings.py
    def get_serializer_context(self):
        return {'request':self.request}
    
    def delete(self, request, pk):
            product=get_object_or_404(Product, id=pk)
            if product.orderitems.count()>0:
                return Response({'error':'product cannot be deleteted because it is associated with an order item.'}
                                ,status=status.HTTP_405_METHOD_NOT_ALLOWED)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
                            
                
class CollectionViewSet(ModelViewSet):
                
    serializer_class=CollectionSerializer
    queryset=Collection.objects.annotate(products_count=Count('products'))
   
    permission_classes=[IsAdminOrReadOnly]
    def delete(self, request, pk):
        collection=get_object_or_404(Collection.objects.annotate(products_count=Count('products')), id=pk)
        if collection.products.count()>0:
            return Response({'error':'collection cannot be deleteted because it is associated with a product.'}
                            ,status=status.HTTP_405_METHOD_NOT_ALLOWED
                            )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def get_serializer_context(self):
        return {'request':self.request}
          
        
class ReviewSet(ModelViewSet):
    serializer_class=ReviewSerializer
    
    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}   
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
  
                 
                   
class CartViewSet(CreateModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  GenericViewSet): #we just need create, get and delete, and no list so we should not inherit from modelviewset 
    queryset=Cart.objects.prefetch_related('items__product').all()
    serializer_class=CartSerializer
    
    
class CartItemViewSet(ModelViewSet):
    http_method_names=['get','post','patch','delete'] # to prevent put request, as we just want to update the quantity of an item
    def get_serializer_class(self):
        if self.request.method=='POST':
            return CartItemAddSerializer
        elif self.request.method=='PATCH':
            return CartItemUpdateSerializer
        else:
            return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id':self.kwargs['cart_pk']}   
    def get_queryset(self):
        return CartItem.objects.\
            filter(cart_id=self.kwargs['cart_pk']).select_related('product') # to make an inner join between the cart items and products, onless there would be an extra query for each cart item to get the related product
            
class CustomerViewSet(ModelViewSet): 
   
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    permission_classes=[IsAdminUser]
    # def get_permissions(self):
    #     if self.request.method=='GET':
    #         return [AllowAny()]
    #     return [IsAuthenticated()]
        
            
    @action(detail=False, methods=['GET','PUT'], permission_classes=[IsAuthenticated])
    def me(self,request):
        customer=Customer.objects.get(user_id=request.user.id)
        if request.method== 'GET':
            serializer=CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer=CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)     
   
     
class  OrderViewSet(ModelViewSet):
    http_method_names=['get','patch','delete','post','head','options']
    
    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    def create(self, request, *args, **kwargs): #overriding the create function of modelviewset class to return OrderSerializer instead of OrderCreateSerializer
            serializer=OrderCreateSerializer(data=request.data,
                                            context={'user_id': self.request.user.id} )
            serializer.is_valid(raise_exception=True)
            order=serializer.save()
            serializer=OrderSerializer(order)
            return Response(serializer.data)
        
    def get_serializer_class(self):
        if self.request.method=='POST':
            return OrderCreateSerializer
        elif self.request.method=='PATCH':
            return OrderUpdateSerializer
        else:
            return OrderSerializer
        
    def get_queryset(self):
        user=self.request.user
        if user.is_staff:
            return  Order.objects.all()
        else:
            current_customer_id=Customer.objects.only('id').get(user_id=user.id)# to prevent exception when there is no customer related to the user
            return Order.objects.filter(customer_id=current_customer_id)
    
    
        
class OrderItemViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer
        
# Create your views here.
#restful APIs:


# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method=='GET':
#         queryset=Product.objects.all()
#         serializer=ProductSerializer(queryset, many=True, context={'request':request})
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer=ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ProductList(ListCreateAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer

# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer

#     def delete(self, request, pk):
#         product=get_object_or_404(Product, id=pk)
#         if product.orderitems.count()>0:
#             return Response({'error':'product cannot be deleteted because it is associated with an order item.'}
#                             ,status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# @api_view(['GET','PUT', 'DELETE'])
# def product_detail(request, pk):
 
#     product=get_object_or_404(Product, id=pk)
#     if request.method=='GET':
#         serializer=ProductSerializer(product, context={'request':request})
#         return Response(serializer.data)
#     elif request.method=='PUT':
#         serializer=ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method=='DELETE':
#         if product.orderitems.count()>0:
#             return Response({'error':'product cannot be deleteted because it is associated with an order item.'}
#                             ,status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
        
        
#The following api views are implemented as class-based view later
# @api_view(['GET','PUT', 'DELETE'])
# def collection_detail(request, pk):
#     collection=get_object_or_404(Collection.objects.annotate(products_count=Count('products')), id=pk)

#     if request.method=='GET':
#         serializer=CollectionSerializer(collection)
#         return Response(serializer.data)
#     elif request.method=='PUT':
#         serializer=CollectionSerializer(collection, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method=='DELETE':
#         if collection.products.count()>0:
#             return Response({'error':'collection cannot be deleteted because it is associated with a product.'}
#                             ,status=status.HTTP_405_METHOD_NOT_ALLOWED
#                             )
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def collection_list(request):
#     if request.method=='GET':
#         collections=Collection.objects.annotate(products_count=Count('products')).all()
#         serializer=CollectionSerializer(collections, many=True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer=CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#class based views of the above comment:
# class CollectionDetail(APIView):

#     def get(self, request, pk):
#         collection=get_object_or_404(Collection.objects.annotate(products_count=Count('products')), id=pk)
#         serializer=CollectionSerializer(collection)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         collection=get_object_or_404(Collection.objects.annotate(products_count=Count('products')), id=pk)
#         serializer=CollectionSerializer(collection, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def delete(self, request, pk):
#         collection=get_object_or_404(Collection.objects.annotate(products_count=Count('products')), id=pk)
#         if collection.products.count()>0:
#             return Response({'error':'collection cannot be deleteted because it is associated with a product.'}
#                             ,status=status.HTTP_405_METHOD_NOT_ALLOWED
#                             )
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#collectionDetail calsss using generic views:

# class CollectionDetail(RetrieveUpdateDestroyAPIView):
   
#     serializer_class=CollectionSerializer
#     queryset=Collection.objects.annotate(products_count=Count('products'))
   
   
#     def delete(self, request, pk):
#         collection=get_object_or_404(Collection.objects.annotate(products_count=Count('products')), id=pk)
#         if collection.products.count()>0:
#             return Response({'error':'collection cannot be deleteted because it is associated with a product.'}
#                             ,status=status.HTTP_405_METHOD_NOT_ALLOWED
#                             )
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CollectionList(APIView):
#     def get(self, request):
#         collections=Collection.objects.annotate(products_count=Count('products')).all()
#         serializer=CollectionSerializer(collections, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer=CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
#the above class using listCreateApiView


# class CollectionList(ListCreateAPIView):
#     queryset=Collection.objects.annotate(products_count=Count('products')).all()
#     serializer_class=CollectionSerializer
    
#     # def get_queryset(self):
#     #     return Collection.objects.annotate(products_count=Count('products')).all()
    
#     # def get_serializer_class(self):
#     #     return CollectionSerializer
   
#     def get_serializer_context(self):
#         return {'request':self.request}
    
