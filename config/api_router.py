from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from brain_health.users.views import UserViewSet, TherapistDetailViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("therapist", TherapistDetailViewSet)


app_name = "api"
urlpatterns = router.urls

