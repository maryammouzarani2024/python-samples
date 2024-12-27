from decimal import Decimal
from django.db import transaction
from rest_framework import serializers

from .models import Product, Customer, Collection, Review, Cart, CartItem, Order, OrderItem

# a sample of bad practice, it is better to use modelserializer
# class CollectionSerializer(serializers.Serializer):
#     # id=serializers.IntegerField()
#     # title=serializers.CharField(max_length=255)
    
class CollectionSerializer(serializers.ModelSerializer):  
    class Meta:
        model=Collection
        fields=['id', 'title', 'products_count']
        
    products_count=serializers.IntegerField(read_only=True)
    
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id', 'description','title','price', 'price_with_tax', 'collection', 'inventory']
        
    price_with_tax=serializers.SerializerMethodField(method_name='calculate_tax')
    # collection=serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection_detail'
    # )
    def calculate_tax(self, product:Product):
        return product.price*Decimal(1.1)
    
    #customizing post creation method, this function is called by save() function of the serializer
    def create(self, validated_data):

        product=Product(**validated_data)
        product.price +=Decimal(0.01)
        product.save()
        return product

    #customizing put update method
    def update(self, instance:Product, validated_data):
        instance.price=validated_data.get('price')+Decimal(0.01)
        instance.save()
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['id','date' ,'name', 'description']
        
    def create(self, validated_data):
            product_id=self.context['product_id']
            return Review.objects.create(product_id=product_id, **validated_data)
        

class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta: 
        model=CartItem
        fields=['quantity']

class CartItemSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    total_price=serializers.SerializerMethodField()
    class Meta:
        model=CartItem
        fields=['id','product','quantity','total_price']
    
    def get_total_price(self, cart_item:CartItem):
        return cart_item.quantity *cart_item.product.price
    
    def create(self, validated_data):
            cart_id=self.context['cart_id']
            return CartItem.objects.create(cart_id=cart_id, **validated_data)
    

class CartItemAddSerializer(serializers.ModelSerializer):
    product_id=serializers.IntegerField()# this field is generated dynamically at runtime, so should be explicitly defined here
    
    class Meta:
        model=CartItem
        fields=['id', 'product_id', 'quantity']
    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError("No product with this id found.")
        else:
            return value
    def save(self, **kwargs):
        cart_id=self.context['cart_id']
        print("***************")
        print("cart id:" , cart_id)
        product_id=self.validated_data['product_id']
        quantity=self.validated_data['quantity']   
        #save the new cart item:
        try:
            cart_item=CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            #update existing cart item:
            cart_item.quantity+= quantity
            cart_item.save()
            self.instance=cart_item
        except CartItem.DoesNotExist:
            #create a new cart item
            self.instance=CartItem.objects.create(cart_id=cart_id,**self.validated_data)
        return self.instance
class CartSerializer(serializers.ModelSerializer):
    id=serializers.UUIDField(read_only=True)   
    items=CartItemSerializer(many=True, read_only=True)
    total_price=serializers.SerializerMethodField()
    
    class Meta:
           model=Cart 
           fields=['id', 'items','total_price']
    
    def get_total_price(self, cart:Cart):
        return sum([item.quantity * item.product.price for item in cart.items.all() ])
    

class CustomerSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(read_only=True)
    class Meta:
        model=Customer
        fields=['id', 'user_id','phone','birth_date','membership']



# Order Serializers:

class OrderItemSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    class Meta:
        model=OrderItem
        fields=['id','product', 'unit_price','quantity']


class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True)
    class Meta:
        model=Order
        fields=['id','customer','placed_at','payment_status', 'items' ]

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['payment_status']

class OrderCreateSerializer(serializers.Serializer):# need a specific serializer to create an order from a shopping cart
    cart_id=serializers.UUIDField()
    
    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError("No cart with this id found.")
        if CartItem.objects.filter(cart_id=cart_id).count()==0:
            raise serializers.ValidationError("The cart is empty.")
        else:
            return cart_id
        
    def save(self, **kwargs):
        with transaction.atomic():
            cart_id=self.validated_data['cart_id']
            user_id=self.context['user_id']
            print(user_id, cart_id)
            customer=Customer.objects.get(user_id=user_id)
            
            #create an order 
            order=Order.objects.create(customer=customer)
            
            #inserting the cart items into the order
            cartItems=CartItem.objects.select_related('product').filter(cart_id=cart_id)
            
            # for item in cartItems:
            #     orderItem=OrderItem.objects.create(
            #         order_id=order.id,
            #         product=item.product, 
            #         quantity=item.quantity,
            #         unit_price=item.product.price
            #     )
            # cleaner:
            order_items=[
                OrderItem(
                    order=order, 
                    product=item.product, 
                    unit_price=item.product.price,
                    quantity=item.quantity                
                ) for item in cartItems
            ]
            
            OrderItem.objects.bulk_create(order_items)
            Cart.objects.get(pk=cart_id).delete()    
            return order
            
                    