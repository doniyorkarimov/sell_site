from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register("users",CustomUserModelViewSet,basename="users")
router.register("category", CategoryModelViewSet, basename="category"),
router.register("product", ProductCreateModelViewSet, basename="product"),
router.register("ichki_category",IchkicategoryModelViewSet, basename='ichki_category')

urlpatterns = [
    path("",include(router.urls)),
]