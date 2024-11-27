from django.db import models
from django.contrib.auth.models import AbstractUser
from mptt.models import MPTTModel,TreeForeignKey
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
STATUS = (
        ('user', 'user'),
        ('admin', 'Admin')

    )

class CustomUser(AbstractUser):
    status = models.CharField(choices=STATUS, max_length=60, default='user')
    number = models.CharField(max_length=25)


class Photo(models.Model):
    rasm = models.ImageField(null=True, default="images.png")


class Register(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)




class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    birth_date = models.DateTimeField()
    gender_choices = [
        ('male', 'Erkak'),
        ('female', 'Ayol'),
    ]
    gender = models.CharField(max_length=6, choices=gender_choices)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)

class Category1(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='category_img')    

class Category(MPTTModel):
    name = models.CharField(_("Name"), max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    photo = models.ImageField(upload_to='category_img')
    slug = models.SlugField(max_length=10, unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            num=10000 + self.id
            self.slug = f"{slugify(self.name)}-{num}"
        super().save(*args, **kwargs)

class CategoryAttribute(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='attributes')
    name = models.CharField(_("Attribute Name"), max_length=100)

class Product(models.Model):
    name = models.CharField(_("product name"), max_length=200)
    photo = models.ImageField(upload_to='product_img')
    description = models.TextField(_("description"), null=True, blank=True)
    price = models.DecimalField(_("product Price"), max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            num=90100 + self.id
            self.slug = f"{slugify(self.name)}-{num}"
        super().save(*args, **kwargs)

class SavatItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    soni = models.IntegerField(default=1)    

class Savat(models.Model):
    savat_item=models.ManyToManyField(SavatItem,blank=True,related_name="savat_item")
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class AttributeValue(models.Model):
    attribute = models.ForeignKey(CategoryAttribute, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(_("Value"), max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_values")
  