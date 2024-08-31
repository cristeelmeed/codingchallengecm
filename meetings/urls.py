from django.urls import path
from .views import AvaliableEmployeeView

urlpatterns = [
    path('available-times/', AvaliableEmployeeView.as_view(), name='available-times'),
]