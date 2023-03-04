from rest_framework.routers import DefaultRouter
from login.api.views.views_users import userViewSet

router = DefaultRouter()
router.register('', userViewSet, basename="user")
# router.register('',userRetrieveViewSet, basename= "change")
urlpatterns = router.urls