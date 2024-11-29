"""
URL configuration for pizzaOrder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from pizza import views as pizza_views
from pizza import api_views as pizza_api_views
from home import views as home_views
from customer import views as customer_views
from exceptionhandler.views import handler_404, handler_500, handler_403

handler404=handler_404
handler500=handler_500
handler403=handler_403


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_views.home, name='home' ),
    path('login', home_views.LoginInterfaceView.as_view(), name='login' ),
    path('logout', home_views.LogoutInterfaceView.as_view(), name='logout' ),
    path('signup', home_views.signup, name='signup' ),
    path('checkout', home_views.checkout, name='checkout' ),
    
    path('profile', customer_views.profile, name='profile' ),
    path('<int:pk>/edit_order', customer_views.OrdersUpdateView.as_view(), name='edit_order' ),
    
    
    path('pricing',pizza_views.pricing, name='pricing' ),

    path('comments/', include('notes.urls')),

    path('api/pizzas', pizza_api_views.PizzaAPIList.as_view()),
    path('api/pizzas/new', pizza_api_views.PizzaCreate.as_view()),
    path('api/pizzas/<int:id>/', pizza_api_views.PizzaUpdate.as_view()),
] 
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)