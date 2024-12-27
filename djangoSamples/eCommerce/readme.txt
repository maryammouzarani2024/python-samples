This is complete example of the back-end of an online store.
The APIs are implemented using django rest framework. 



Installation
------------

pip install -r requirements.txt



Execution
---------

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver


Create New User API:
post the new user info to http://127.0.0.1:8088/auth/users/

Login:
post the user info to http://127.0.0.1:8000/auth/jwt/create

Check the current user:
get http://127.0.0.1:8088/auth/users/me

View the list of products:
get http://127.0.0.1:8088/store/products

Create a new shopping cart:
post a request to http://127.0.0.1:8088/store/carts

other APIs are listed at http://127.0.0.1:8088/store

Have fun!