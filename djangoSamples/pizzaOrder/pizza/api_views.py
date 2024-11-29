from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView,  RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError
from django.core.cache import cache

#Enabling pagination:
from rest_framework.pagination import LimitOffsetPagination



from .serializar import PizzaSerializer
from .models import Pizza


#Cursor pagination is the best performance choice for paginating large data sets
class PizzaPagination(LimitOffsetPagination):
    default_limit=10
    max_limit=100


class PizzaAPIList(ListAPIView):
    queryset=Pizza.objects.all()
    serializer_class=PizzaSerializer

    #set a filter by id fields
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields=['id']
    search_fields=['topping1','title']
    pagination_class=PizzaPagination


    def get_queryset(self):

        discounted=self.request.query_params.get('discounted',None)
        if discounted is None:
            return super().get_queryset()
        queryset= Pizza.objects.all()
        if discounted.lower()=='true':
            return queryset.filter(discount=True)
        return queryset.filter(discount=False)

        
#create API View class:
#curl script to create a new pizza:
#curl -X post http://localhost:8000/api/pizzas/new/ -d price=12 -d title='newPizza' -d topping1='cheese' -d topping2='Salami' -d discounted=False 


class PizzaCreate(CreateAPIView):
    serializer_class=PizzaSerializer

    #overwriting the create method to control the price value not being negative or zero
    def create(self, request, *args, **kwargs ):
        try:
            price=float(request.data.get('price'))
            if price is not None and price <=0:
                raise ValidationError({'price':'The price must be more than 0$'})
        except ValueError:
            raise ValidationError({'price':'The price is not valid'})
        return super().create(request, *args, **kwargs)
    

#destroy API
#curl script to destroy pizza with id 6
# curl -X DELETE http://localhost:8000/api/pizzas/6/delete

# class PizzaDestroy(DestroyAPIView):
#     queryset=Pizza.objects.all()
#     lookup_field='id'

#     #to also delete the cache:
#     def delete(self, request, *args, **kwargs):
#         pizza_id=request.data.get('id')
#         response=super().delete(request, *args, **kwargs)

#         if response.status_code==204:
#             cache.delete('pizza_data_{}'.format(pizza_id))
#         return response

#we can also use a RetrieveUpdateDestroyAPIView class to merge the update and destroy methods and have a single url 
class PizzaUpdate(RetrieveUpdateDestroyAPIView):
    queryset=Pizza.objects.all()
    lookup_field='id'
    serializer_class=PizzaSerializer
    
    
    #to also delete the cache:
    def delete(self, request, *args, **kwargs):
        pizza_id=request.data.get('id')
        response=super().delete(request, *args, **kwargs)

        if response.status_code==204:
            cache.delete('pizza_data_{}'.format(pizza_id))
        return response

    def update(self, request, *args, **kwargs):
            response=super().update(request, *args, **kwargs)
            if response.status_code==200:
               pizza=response.data
               cache.set('pizza_data_{}'.format(pizza['id']), {
                   'title':pizza['title'],
                   'topping1':pizza['topping1'],
                   'topping2':pizza['topping2'],
                   'size':pizza['size'],
                   'price':pizza['price'],
                   'image':pizza['image'],
                   'discount':pizza['discount'],
                   'discount_value':pizza['discount_value'] 
                   }                    
                )
            return response