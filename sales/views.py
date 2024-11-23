from rest_framework.response import Response 
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework_simplejwt.tokens  import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from .models import *
from .serilazer import  *
        


from rest_framework.viewsets import ModelViewSet

class CustomUserModelViewSet(ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSer
    permission_classes=[IsAuthenticated]


class USerProfileModelViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfilSer

class ProductSerModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSer

class Category1ModelViewSet(ModelViewSet):
    queryset = Category1.objects.all()
    serializer_class = Category1Ser

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySer

class CategoryAttributeModelViewSet(ModelViewSet):
    queryset = CategoryAttribute.objects.all()
    serializer_class = CategoryAttributSer

class AttributeValueModelViewSet(ModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSer

class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSer


# # class CategoryPagination(PageNumberPagination):
# #     page_size = 20
# #     page_size_query_param = 'page_size' 
# #     max_page_size = 100  





   


         