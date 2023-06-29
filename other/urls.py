from django.urls import path

from .views import CurrentDataView, HelloWorld, RandomNumber, IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    path('datetime/', CurrentDataView.as_view()),
    path('hello/', HelloWorld.as_view()),
    path('random/', RandomNumber.as_view()),

]
