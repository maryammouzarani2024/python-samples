from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator 
from guardian.shortcuts import assign_perm 

from pizza.models import Pizza
# Create your models here.
#run this for existing users who has no customer
# python manage.py shell
# from django.contrib.auth.models import User
# from customer.models import Customer
# for user in User.objects.all(): Customer.objects.create(user=user, address="aa", post_code="1212", phone=323)

#to preserve the customer's privacy, their addresses are stored encrypted
class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    address=models.CharField(max_length=255)
    post_code=models.CharField(max_length=30)
    phone=PhoneNumberField()
    profile_photo=models.ImageField(upload_to="images/profile_images/", null=True)
    def __str__(self) -> str:
        return str(self.user.first_name)


@receiver(post_save, sender=User)
def update_customer_signal(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
    instance.customer.save()



class OrderRecords(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE, default=None, null=True)
    time=models.TimeField(auto_now=True)
    order_date=models.DateTimeField(auto_now=True)
    pizza_order=models.ForeignKey(Pizza, on_delete=models.CASCADE)
    number=models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    final_price=models.FloatField(default=1, validators=[MinValueValidator(1.0)])
    extra_topping1=models.CharField(max_length=255, null=True, blank=True)
    extra_topping2=models.CharField(max_length=255, null=True, blank=True)
    other_wishes=models.CharField(max_length=255, null=True, blank=True)
   
    def __str__(self) -> str:
        return str(self.time)

# #each user can edit its own orders
# @receiver(post_save, sender=OrderRecords)
# def set_notes_permissions(sender, instance, **kwargs):
#     user=User.objects.get(username=instance.customer.user.username)
#     assign_perm('order.change_order', user)
#     assign_perm('order.change_order', user, instance)