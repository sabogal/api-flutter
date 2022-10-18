from rest_framework.routers import DefaultRouter
from login.views import userViewSet

router = DefaultRouter()
router.register('', userViewSet, basename="user")
# router.register('',userRetrieveViewSet, basename= "change")
urlpatterns = router.urls