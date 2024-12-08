from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # wroks like router

router.register('', views.ContactusViewset) # works like antena
urlpatterns = [
    path('', include(router.urls)),
]