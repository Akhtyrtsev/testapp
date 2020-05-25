from django.urls import path, include, re_path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()

router.register('users', views.UserViewSet, basename='user')
router.register('courses', views.CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
    ]