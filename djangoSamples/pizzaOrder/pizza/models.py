from django.db import models

# Create your models here.
class Size(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

class Pizza(models.Model):
    title=models.CharField(max_length=150, default='pizza')
    topping1=models.CharField(max_length=100)
    topping2=models.CharField(max_length=100)
    size=models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    image=models.ImageField(upload_to="images/", null=True)
    price=models.FloatField(default=0)
    discount=models.BooleanField(default=False)
    discount_value=models.IntegerField(default=0)
    
    
    def __str__(self) -> str:
        return self.title