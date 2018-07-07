from django.conf.urls import url,include
from rest_framework_nested import routers
from user import views


router = routers.SimpleRouter()
router.register(r'country_code_lookups',views.CountryCodeLookupsViewSet)
router.register(r'users',views.UserViewSet)
user_router = routers.NestedSimpleRouter(router,r'users',lookup='user')
user_router.register(r'user_general_info',views.UserGeneralInfoViewSet)


urlpatterns=[
    url(r'',include(router.urls)),
    url(r'',include(user_router.urls))
]