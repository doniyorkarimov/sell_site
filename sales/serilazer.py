from rest_framework import serializers
from .models import *
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
        fields = ["id",'username', 'password', 'number',"user_extra_data"]
        extra_kwargs = {'password' : {'write_only': True}}
    


class UserProfilSer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields= ['user','name', 'family','father_name','birth_date','gender', 'email','phone_number']


class Category1Ser(serializers.ModelSerializer):
    class Meta:
        model = Category1
        fields = ['name','photo']

class CategorySer(serializers.ModelSerializer):
    class Meta:
        model = Category     
        fields = ['id', 'name', 'photo','parent', 'slug']

class CategoryAttributSer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAttribute
        fields = ['category', 'name']


class AttributeValueSer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = "__all__"


class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {'user':{'read_only': True}}
    


class SavatSer(serializers.ModelSerializer):
    class Meta:
        model = Savat
        fields = ['savat_item','user']


class SavatItemSer(serializers.ModelSerializer):
    class Meta:
        model = SavatItem
        fields = ['product','soni']


class CommentSer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user','product', 'content','created_at']

        
