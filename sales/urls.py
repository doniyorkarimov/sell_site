from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register("users",CustomUserModelViewSet,basename="users")
router.register("product",ProductSerModelViewSet,basename="product")
router.register("category1",Category1ModelViewSet,basename="category1")
router.register("category_attribute",CategoryAttributeModelViewSet,basename="category_attribute/")
router.register("category",CategoryModelViewSet,basename="category")
router.register("attribute",AttributeValueModelViewSet,basename="attribute")
router.register("comment",CommentModelViewSet,basename="comment")



urlpatterns = [
    path("",include(router.urls)),
]