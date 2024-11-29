 mkdir pizzaOrder
 cd pizzaOrder/
 1425  python3 -m venv venv
 1426  source venv/bin/activate
 1427  pip3 install django
 1428  django-admin startproject
 1429  django-admin startproject pizzaOrder
 1430  mv pizzaOrder/ pizzaOrder-projects
 1431  ls
 1432  cd pizzaOrder-projects/
 1433  python3 manage.py runserver

 working with form widgets
 uploading images in the forms
 dynamic multiple forms on a page

 for using css:
 pip install django-widget-tweaks

 to-does:
 add pizzas to the database- pizza with name, materials and photos
 in the home page 3 pizzas 
 add users as customers: address, 
 add orders to the database
 the possibility to edit orders in 30 minutes
 add profiles: view previous orders.