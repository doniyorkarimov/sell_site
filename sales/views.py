from rest_framework.response import Response 
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework_simplejwt.tokens  import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from .models import *
from .serilazer import CategorySer, SavatSer, ProductSer, Product_imgSer, CustomUserSer, IchkicategorySer

from rest_framework.viewsets import ModelViewSet

class CustomUserModelViewSet(ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSer
    permission_classes=[AllowAny]


class IchkicategoryModelViewSet(ModelViewSet):
    queryset = Ichkicategory.objects.all()
    serializer_class = IchkicategorySer

# class CategoryPagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size' 
#     max_page_size = 100  

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySer


class ProductCreateModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSer
   


         