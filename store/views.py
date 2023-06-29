from django.shortcuts import render
from django.views import View


class ProductSingleView(View):
    def get(self, request):
        return render(request, 'store/product-single.html')


class CartView(View):
    def get(self, request):
        return render(request, 'store/cart.html')


class ShopView(View):
    def get(self, request):
        context = {'data': [
            {'name': 'Bell  Papper',
             'discount': 30,
             'price_before': 120.00,
             'price_after': 80.00,
             'url': 'store/images/product-1.jpg'},
            {'name': 'Strawberry',
             'discount': None,
             'price_before': 120.00,
             'url': 'store/images/product-2.jpg'},
            {'name': 'Green Beans',
             'discount': None,
             'price_before': 120.00,
             'url': 'store/images/product-3.jpg'},
            {'name': 'Purple Cabbage',
             'discount': None,
             'price_before': 120.00,
             'url': 'store/images/product-4.jpg'}
            ]
        }
        return render(request, 'store/shop.html', context)