from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router_user = DefaultRouter()
router_user.register(r'', User_ViewSet, basename='User')

router_category = DefaultRouter()
router_category.register(r'', Category_ViewSet, basename='Category')

router_trademark = DefaultRouter()
router_trademark.register(r'', Trademark_ViewSet, basename='Trademark')

router_made = DefaultRouter()
router_made.register(r'', Made_ViewSet, basename='Made')

router_product = DefaultRouter()
router_product.register(r'', Product_ViewSet, basename='Product')

router_stock = DefaultRouter()
router_stock.register(r'', Stock_ViewSet, basename='Stock')

router_grn = DefaultRouter()
router_grn.register(r'', Goods_received_note_ViewSet, basename='Goods_received_note')

router_cart = DefaultRouter()
router_cart.register(r'', Cart_ViewSet, basename='Cart')

router_cart_detail = DefaultRouter()
router_cart_detail.register(r'', Cart_detail_ViewSet, basename='Cart_detail')

router_order = DefaultRouter()
router_order.register(r'', Oder_ViewSet, basename='Oder')

router_order_detail = DefaultRouter()
router_order_detail.register(r'', Oder_detail_ViewSet, basename='Oder_detail')

urlpatterns = [
    path('User/', include(router_user.urls)),
    path('Category/', include(router_category.urls)),
    path('Trademark/', include(router_trademark.urls)),
    path('Made/', include(router_made.urls)),
    path('Product/', include(router_product.urls)),
    path('Stock/', include(router_stock.urls)),
    path('Goods_received_note/', include(router_grn.urls)),
    path('Cart/', include(router_cart.urls)),
    path('Cart_detail/', include(router_cart_detail.urls)),
    path('Oder/', include(router_order.urls)),
    path('Oder_detail/', include(router_order_detail.urls)),

    path('add_detail_cart/', add_detail_cart),
    path('change_amount/',change_amount),
    path('add_Oder/',add_Oder),
    path('list_product_AI/',product_suggest),

]