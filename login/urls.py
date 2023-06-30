from django.urls import path

from .views import LoginSingleView


urlpatterns = [
    path('', LoginSingleView.as_view()),

]