from django.db import models
from django.contrib.auth.models import AbstractUser
from mptt.models import MPTTModel,TreeForeignKey

STATUS = (
        ('user', 'user'),
        ('admin', 'Admin')

    )


class CustomUser(AbstractUser):
    status = models.CharField(choices=STATUS, max_length=60, default='user')

class Category(models.Model):
    name = models.CharField(max_length=300)
    parent = TreeForeignKey('self', verbose_name = 'ichki tur', on_delete = models.CASCADE, null=True, blank=True)
    rasm = models.ImageField(upload_to='category.img', null=True, blank=True)
    level = models.PositiveIntegerField(default=0) 

    class MPTTMeta:
        order_insertion_by = ['name']

class Ichkicategory(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ichki_category')



class Product(models.Model):
    name = models.CharField(max_length=100)
    sharx = models.TextField()
    price = models.TextField()
    category = models.ForeignKey(Ichkicategory,verbose_name = 'category', on_delete=models.CASCADE, related_name='productlar')  
    user = models.ForeignKey(CustomUser,verbose_name='customuser', on_delete=models.CASCADE, related_name='product',null=True)
    createtime = models.DateTimeField(auto_now_add=True)  

class Product_img(models.Model):
    rasm = models.ImageField(null=True)

class SavatItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    soni = models.IntegerField(default=1)    

class Savat(models.Model):
    savat_item=models.ManyToManyField(SavatItem,blank=True,related_name="savat_item")
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)



class Register(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)






class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.product}"


    
