from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('list', views.UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('register/',views.UserRegistration.as_view(),name='register'),
    path('active/<uid>/<token>/',views.Activate.as_view(),name='activate'),
    path('login/',views.UserLoginView.as_view(),name="login"),
    path('logout/',views.UserLogOutView.as_view(),name="logout")
]