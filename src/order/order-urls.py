from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tax-invoice', views.TaxInvoiceViewset, base_name='tax-invoice')
router.register(r'tax', views.TaxViewset, base_name='tax')
router.register(r'shipping', views.OrderShippingViewset, base_name='shipping')
router.register(r'', views.OrderViewset, base_name='order')


urlpatterns = router.urls