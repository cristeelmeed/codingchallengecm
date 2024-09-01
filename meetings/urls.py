from django.urls import path
from .views import AvaliableEmployeeView

urlpatterns = [
    path('available-meeting/', AvaliableEmployeeView.as_view(), name='available-meeting'),
]