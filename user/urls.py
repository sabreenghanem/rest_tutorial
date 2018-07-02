from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from user import views

router = DefaultRouter()
router.register(r'country_code_lookups',views.CountryCodeLookupsViewSet)
router.register(r'users',views.UserViewSet)
urlpatterns=[
    url(r'',include(router.urls))
]