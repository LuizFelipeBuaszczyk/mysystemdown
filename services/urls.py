from rest_framework.routers import DefaultRouter

from services.views.service_view import ServiceViewSet

router = DefaultRouter()
router.register(r"", ServiceViewSet, basename="services")

urlpatterns = router.urls