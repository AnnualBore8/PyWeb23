from django.urls import path

from .views import LoginSingleView, LogoutView, CreateAccountView


app_name = 'login'  # позволяет base.html построить полный адрес (показывает, что мы обращаемся именно сюда)

urlpatterns = [
    path('', LoginSingleView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', CreateAccountView.as_view(), name='create'),

]