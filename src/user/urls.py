"""
    User App URLs
"""

from rest_framework import routers
from .views import (UserViewSet)


router = routers.SimpleRouter()
router.register(r'', UserViewSet)
urlpatterns = router.urls
