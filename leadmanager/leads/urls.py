from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register('api/leads', api.LeadViewSet, 'leads')

urlpatterns = router.urls
