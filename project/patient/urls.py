from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('list', views.UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('register/',views.UserRegistration.as_view(),name='register')
]