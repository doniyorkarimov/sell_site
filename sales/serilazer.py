from rest_framework import serializers
from .models import Category, Product, Product_img, Savat, Ichkicategory
from .models import CustomUser


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['user_id'] = user.id

        # ...

        return token


class CustomUserSer(serializers.ModelSerializer):
    user_extra_data=serializers.SerializerMethodField(read_only=True)
    
    def get_user_extra_data(self,obj):
        user_savat=Savat.objects.filter(user=obj)
        print(user_savat)
        if user_savat:
            result=0
            for i in user_savat.savat_item:
                result+=i.soni*i.product.price
            return result
        
    class Meta:
        model = CustomUser  
        fields = ["id",'username', 'password' ,"user_extra_data"]
        extra_kwargs = {'password' : {'write_only': True}}
    




class CategorySer(serializers.ModelSerializer):
    class Meta:
        model = Category     
        fields = ['id', 'name', 'rasm','parent']
    

class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {'user':{'read_only': True}}
    


class IchkicategorySer(serializers.ModelSerializer):
    class Meta:
        model = Ichkicategory
        fields = ['Category']

class SavatSer(serializers.ModelSerializer):
    class Meta:
        model = Savat
        fields = ['product','soni']

class Product_imgSer(serializers.ModelSerializer):
    class meta:
        model = Product_img
        fields = ['rasm', 'product']




        
