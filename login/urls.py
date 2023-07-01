from django.urls import path

from .views import LoginSingleView, LogoutView


urlpatterns = [
    path('', LoginSingleView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),

]