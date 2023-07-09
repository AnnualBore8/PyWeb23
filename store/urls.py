from django.urls import path

from .views import ProductView, CartView, ShopView, CartViewSet,\
    WishlistView, WishListViewSet, AddToWishList, RemoveFromWishList

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)

router.register(r'wishlist', WishListViewSet)

app_name = 'store'

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('product/<int:id>/', ProductView.as_view(), name='product'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('wishlist/add/<int:id>/', AddToWishList.as_view(), name='addtowishlist'),
    path('wishlist/remove/<int:id>', RemoveFromWishList.as_view(), name='remove_wish_list'),

]
