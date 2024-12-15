from django.urls import include,path
from rest_framework import routers
from .views import AvailableTimeViewSets,DesignationViewSets,DoctorViewSets,ReviewViewSets,SpecializationViewSets
router=routers.DefaultRouter()

router.register('availabletime', AvailableTimeViewSets)
router.register('designation',DesignationViewSets)
router.register('list',DoctorViewSets)
router.register('review',ReviewViewSets)
router.register('specialization',SpecializationViewSets)
urlpatterns = [
    path('', include(router.urls)),
]