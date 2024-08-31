from rest_framework import routers
from .api import MeetingViewSet

router = routers.DefaultRouter()

router.register('api/meetings', MeetingViewSet, 'meetings')

urlpatterns = router.urls