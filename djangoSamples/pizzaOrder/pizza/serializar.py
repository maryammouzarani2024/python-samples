from rest_framework import serializers
from .models import Pizza
from customer.models import OrderRecords

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderRecords
        fields=('time', 'order_date','customer')


class PizzaSerializer(serializers.ModelSerializer):
    current_price=serializers.FloatField(read_only=True)
    order_info=serializers.SerializerMethodField()
    #control the price value in serializer
    price=serializers.FloatField(min_value=2, max_value=100)
    class Meta:
        model=Pizza
        fields=('id', 'title','topping1', 'topping2', 'price','discount', 'discount_value', 'image','size','current_price','order_info')


    #adding dynamic customized fields to the serializer
    def to_representation(self, instance):
        data=super().to_representation(instance)
        
        data['current_price']=instance.price-((instance.discount_value/100)* instance.price)
       
        return data
    def get_order_info(self, instance):
        orders=OrderRecords.objects.filter(pizza_order=instance)
        return OrderSerializer(orders, many=True).data
