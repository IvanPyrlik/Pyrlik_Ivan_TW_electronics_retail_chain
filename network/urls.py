from django.urls import path, include
from rest_framework.routers import DefaultRouter

from network.views import NetworkViewSet

router = DefaultRouter()
router.register(r"networks", NetworkViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
