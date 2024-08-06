from rest_framework import routers

from .viewsets import personViewSet, productViewSet

router = routers.SimpleRouter()
router.register('person',personViewSet)
router.register('product',productViewSet)

urlpatterns = router.urls