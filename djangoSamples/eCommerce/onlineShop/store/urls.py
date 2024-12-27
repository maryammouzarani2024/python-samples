from django.urls import path
from rest_framework_nested import routers


from . import views


router= routers.DefaultRouter()

router.register('collections',  views.CollectionViewSet)
router.register('products',  views.ProductViewSet, basename='products')
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')


product_router=routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewSet, basename='product-reviews')


cartItem_router=routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cartItem_router.register('items', views.CartItemViewSet, basename='cart-items')


orderItem_router=routers.NestedDefaultRouter(router,'orders', lookup='orders')
orderItem_router.register('items', views.OrderItemViewSet, basename='order-items')
# urlpatterns = [
#     path('products/<int:pk>',  views.ProductDetail.as_view()),
#     path('products/',  views.ProductList.as_view()),
#     path('collections/<int:pk>',  views.CollectionDetail.as_view(), name='collection_detail'),
#     path('collections/',  views.CollectionList.as_view()),
# ]

urlpatterns = router.urls 
urlpatterns+= product_router.urls 
urlpatterns+= cartItem_router.urls 
urlpatterns+=orderItem_router.urls