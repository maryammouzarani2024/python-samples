from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from customer.models import Customer, OrderRecords
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound, HttpResponse


from pizza.models import Pizza
from customer.forms import UserSignupForm, CustomerSignupForm
from notes.models import Notes
import datetime
# Create your views here.


def home(request):
    #revise up users who has no customer:
    for user in User.objects.all():
         if hasattr(user, 'customer')==False:
              Customer.objects.create(user=user, address="aa", post_code="1212", phone=323)
    discounted_pizzas=Pizza.objects.filter(discount=True)
    #get the last 5 comments to show in home page
    # now = datetime.datetime.now()
    # since = datetime.timedelta(days = 20)
    last_five_comments=Notes.objects.all().order_by('-created')[:5]
    return render(request, 'home/home.html', {'discounted_pizzas':discounted_pizzas, 'comments':last_five_comments})


def signup(request):
    userForm=UserSignupForm(request.POST)
    customerForm = CustomerSignupForm(request.POST,request.FILES)
    note=""
    if userForm.is_valid() and customerForm.is_valid():
        user = userForm.save()
        user.refresh_from_db()
        user.customer.address = customerForm.cleaned_data.get('address')
        user.customer.post_code = customerForm.cleaned_data.get('post_code')
        user.customer.phone = customerForm.cleaned_data.get('phone')
        user.customer.profile_photo = customerForm.cleaned_data.get('profile_photo')
        user.save()
        print("user is created")
        note="User is successfully created"
        username = userForm.cleaned_data.get('username')
        password = userForm.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        print("data is incorrect")
        userForm=UserSignupForm(request.POST)
        customerForm = CustomerSignupForm(request.POST)
    return render(request, 'home/signup.html', {'userform': userForm, 'customerform':customerForm,'note':note})



@login_required
def checkout(request):  
    coupons={'new_year':31, 'new_user':9}
    note=""
    if request.method=='POST':
        
        order=OrderRecords()
        customer=get_object_or_404(Customer, user=request.user)
        order.customer=customer
        
        pizza_id=request.POST.get('pizza_id')
        number=request.POST.get('number')
        final_price=request.POST.get('final_price')
        
        if pizza_id:
            try:
                   order.pizza_order=Pizza.objects.get(id=pizza_id)
                   order.number=number
                   order.final_price=final_price
            except Pizza.DoesNotExist:
                 return HttpResponseNotFound
        order.save()
        note="Your order is completed. Enjoy"
        # if pizza discount:
        return render(request, 'home/checkout.html', {'note':note})        
    if request.method=="GET":
        coupon=None     
        number=1
        if 'number' in request.GET:
             number=int(request.GET['number'])
        
        date=datetime.datetime.now()
        if request.GET.get('pizza_id'):
                pizza=get_object_or_404(Pizza,id=request.GET['pizza_id'] )
                final_price=pizza.price
                discount=0
                if 'coupon' in request.GET:
                    if request.GET['coupon'].lower() in coupons:
                        
                        coupon=request.GET['coupon'].lower()
                        print(coupon)
                        percentage=coupons[coupon]
                        coupon_price=int((percentage/100)*pizza.price)
                        discount=coupon_price
                        final_price=pizza.price-coupon_price
                       
                final_price=final_price* number
               # if pizza discount:
                return render(request, 'home/checkout.html', {'title':pizza.title, 
                                                            'topping1':pizza.topping1,
                                                            'topping2':pizza.topping2, 
                                                            'size':pizza.size, 
                                                            'pizza_price':pizza.price,
                                                            'final_price':final_price,
                                                            'discount':discount,
                                                            'id':pizza.id,
                                                            'coupon':coupon,
                                                            'date':date, 
                                                            'number':number
                                                            })        
        else:
                return redirect('home')
class LoginInterfaceView(LoginView):
    template_name='home/login.html'
    success_url='home'
  

class LogoutInterfaceView(LogoutView):
    template_name='home/home.html'
    success_url='home'

