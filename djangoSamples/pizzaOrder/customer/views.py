from django.shortcuts import render
from .models import Customer, OrderRecords
from django.views.generic import UpdateView
from guardian.mixins import PermissionRequiredMixin
from .forms import OrderEditForm
# Create your views here.

from datetime import datetime
def profile(request):
   
    customer=Customer.objects.get(user=request.user)
    orders=OrderRecords.objects.filter(customer=customer)
        
    if request.method=='POST':
        new_first_name=request.POST.get('first_name')
        new_last_name=request.POST.get('last_name')
        new_email=request.POST.get('email')
        new_address=request.POST.get('address')
        new_phone=request.POST.get('phone')

        customer.address=new_address
        customer.phone=new_phone
        customer.user.email=new_email
        customer.user.last_name=new_last_name
        customer.user.first_name=new_first_name
        customer.save()
        customer.user.save()


    now = datetime.now()
    for order in orders:
        if order.order_date.year==now.year and order.order_date.month== now.month and order.order_date.day==now.day and order.order_date.hour==now.hour and (now.minute - order.order_date.minute < 20):
            order.editable=True
            print(order.order_date)
    return render(request, 'customer/profile.html', {'customer':customer, 'orders':orders})

class OrdersUpdateView(UpdateView):
    model=OrderRecords
    form_class=OrderEditForm
    success_url="../profile"
    template_name='customer/order_edit.html'
    # permission_required = 'order.change_order'
    # raise_exception=True
 