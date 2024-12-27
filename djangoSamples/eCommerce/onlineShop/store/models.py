from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from uuid import uuid4
# Create your models here.

class Promotion(models.Model):
    description=models.CharField(max_length=255)
    discount=models.FloatField()
    #product_set: the list of products for a promotion (many-to-many relation)

class Collection(models.Model):
    title=models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
    
class Product(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField(default='-')
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collection, on_delete=models.PROTECT, related_name='products') # if a collection is accidentally deleted, its products should not be deleted
    promotion=models.ManyToManyField(Promotion, blank=True)
    
    def __str__(self):
        return self.title
class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),       
    ]
    
    
    phone=models.CharField(max_length=255)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# the default auth_user_model is the django user model but can be redefined in settings not to be couples with a specific model
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    class Meta:
        ordering=['user__first_name','user__last_name']
class Order(models.Model):
    PAYMENT_PENDING='P'
    PAYMENT_COMPLETED='C'
    PAYMENT_FAILED='F'
    PAYMENT_SATUS_CHOICES=[
        (PAYMENT_COMPLETED,'Completed'),
        (PAYMENT_PENDING,'Pending'),
        (PAYMENT_FAILED,'Failed'),
    ]
    placed_at=models.DateTimeField(auto_now_add=True)   
    payment_status=models.CharField(max_length=1, choices=PAYMENT_SATUS_CHOICES, default=PAYMENT_PENDING)
    customer=models.ForeignKey(Customer, on_delete=models.PROTECT) #if a customer is accidently deleted, the orders should not be deleted

    class Meta:
        permissions=[
            ('cancle_order','can cancle an order')
        ]
class  OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    product=models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orderitems')
    quantity=models.SmallIntegerField()
    unit_price=models.DecimalField(max_digits=6, decimal_places=2)
    

class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)



class Cart(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid4)# to make the cart ids non-guessable
    created_at=models.DateTimeField(auto_now_add=True)
    

class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product=models.ForeignKey(Product, on_delete=models.CASCADE)# if a product is deleted, its relevant cartitem should also be deleted
    quantity=models.SmallIntegerField(
        validators=[MinValueValidator(1)]
    )
    
    class Meta:
        unique_together=[['cart', 'product']] # a product can not exist multiple times in a cart, instead the quantity should be increased
    
class  Review(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name=models.CharField(max_length=255)
    description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)