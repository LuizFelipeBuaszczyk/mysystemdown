from rest_framework.routers import DefaultRouter
from .views import SystemViewSet

router = DefaultRouter()
router.register(r"", SystemViewSet, basename="systems")

urlpatterns = router.urls