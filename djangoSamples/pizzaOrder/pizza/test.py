from rest_framework.test import APITestCase
from django.conf import settings
import os

from .models import Pizza, Size


class PizzaCreateTestCase(APITestCase):
    
    def test_create_pizza(self):
        print("testing create operation...")
        initial_pizza_count=Pizza.objects.count()
        pizza_attr={
            'title':'testPizza',
            'topping1':'aaa',
            'topping2':'aaa',
            
            'topping1':'aaa',
            'price':10,
        }
        response=self.client.post('/api/pizzas/new', pizza_attr)
        if response.status_code != 201:
            print("Not created!!!!")
            print(response.content)
            return
        
        self.assertEqual(
            Pizza.objects.count(),
            initial_pizza_count+1
        )
        print("pass 1st test")
        for attr, expected_value in pizza_attr.items():
            self.assertEqual(
                response.data[attr],expected_value
            )
            print(f"pass test {attr}")
        self.assertEqual(response.data['current_price'], float(pizza_attr['price']))



#testing the destroy operation
class PizzaDestroyTest(APITestCase):

    def test_delete_pizza(self):
        #first create a pizza to make sure the table is not empty:
        print("testing delete operation")
        pizza_attr={
            'title':'testPizza',
            'topping1':'aaa',
            'topping2':'aaa',
            
            'topping1':'aaa',
            'price':10,
        }
        response=self.client.post('/api/pizzas/new', pizza_attr)
        if response.status_code != 201:
            print("Not created!!!!")
            print(response.content)
            return


        initial_pizza_count=Pizza.objects.count()
        
        pizza_id=Pizza.objects.first().id

        self.client.delete('/api/pizzas/{}/'.format(pizza_id))
        self.assertEqual(
            Pizza.objects.count(), 
            initial_pizza_count-1
        )

        self.assertRaises(
            Pizza.DoesNotExist,
            Pizza.objects.get, id=pizza_id,
        )




#testing list api
class PizzaListTestCase(APITestCase):

    def test_list_pizzas(self):
        print("testing list operation ...")

        pizza_count=Pizza.objects.count()
        response= self.client.get('/api/pizzas')

        #the table is empty so the next and previous should be none
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(response.data['count'], pizza_count)
        self.assertEqual(len(response.data['results']), pizza_count)


#testing update api
class PizzaUpdateTestCase(APITestCase):

    def test_update_pizzas(self):
        print("testing delete operation")
        #creating a pizza since the table is empty
        pizza_attr={
            'title':'testPizza',
            'topping1':'aaa',
            'topping2':'aaa',
            
            'topping1':'aaa',
            'price':10,
        }
        response=self.client.post('/api/pizzas/new', pizza_attr)
        if response.status_code != 201:
            print("could not test update!!!!")
            print(response.content)
            return
        
        pizza=Pizza.objects.first()
        updated_fields={
            'title': 'updated',
            'topping1':'new_topping'
        }
        response=self.client.patch('/api/pizzas/{}/'.format(pizza.id), updated_fields, format='json')
        updated_pizza=Pizza.objects.first()
        self.assertEqual(updated_pizza.title, updated_fields['title'])
        self.assertEqual(updated_pizza.topping1, updated_fields['topping1'])


    def test_upload_pizza_image(self):
        print("testing image upload operation")
        #creating a pizza since the table is empty
        pizza_attr={
            'title':'testPizza',
            'topping1':'aaa',
            'topping2':'aaa',
            
            'topping1':'aaa',
            'price':10,
        }
        response=self.client.post('/api/pizzas/new', pizza_attr)
        if response.status_code != 201:
            print("could not test update!!!!")
            print(response.content)
            return
        
        pizza=Pizza.objects.first()
        original_image=pizza.image

        image_path=os.path.join(
            settings.MEDIA_ROOT,
            'images', 'pep.jpg',
        )

        with open (image_path, 'rb') as image_data:
            response=self.client.patch(
                '/api/pizzas/{}/'.format(pizza.id),
                {'image': image_data},
                format='multipart'
            
            )
        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.data['image'], original_image)

        try:
            updated= Pizza.objects.get(id=pizza.id)
            expected_image=os.path.join(
            settings.MEDIA_ROOT,
            'images', 'pep',
            )
            self.assertTrue(updated.image.path.startswith(expected_image))
        finally:
            os.remove(updated.image.path)
