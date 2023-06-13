from django.urls import path
from .views import LocationList, LocationDetail, ItemList, ItemDetail

urlpatterns = [
    path('locations/', LocationList.as_view()),
    path('locations/<int:pk>/', LocationDetail.as_view()),
    path('items/', ItemList.as_view()),
    path('items/<int:pk>/', ItemDetail.as_view()),
]