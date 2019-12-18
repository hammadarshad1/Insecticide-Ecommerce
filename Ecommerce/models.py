from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=20)

    def __str__(self):
        return self.categoryName

class Products(models.Model):
    productId = models.AutoField(primary_key=True)
    productImg = models.ImageField(upload_to='Products', default='default.png')
    productTitle = models.CharField(max_length=50)
    productDescription = models.TextField()
    productRatings = models.FloatField(default=0.0)
    productSales = models.IntegerField(default=0)
    marketPrice = models.FloatField()
    discountedPrice = models.FloatField()
    deliveryCharges = models.FloatField()
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # productStock = models.IntegerField()

    def __str__(self):
        return self.productTitle
    def save(self):
        super().save()

        img = Image.open(self.productImg.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.productImg.path)

class Comments(models.Model):
    commentId = models.AutoField(primary_key=True)
    commentText = models.TextField()
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

class Cart(models.Model):
    cartId = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    productQuantity = models.IntegerField()

class SliderImage(models.Model):
    sliderImgId = models.AutoField(primary_key=True)
    sliderImg = models.ImageField(upload_to='Slider-Image')
    sliderTitle = models.CharField(max_length=30)
    sliderTeaser = models.CharField(max_length=50)

    def save(self):
        super().save()

        img = Image.open(self.sliderImg.path)

        if img.height < 1280 or img.width < 1080:
            output_size = (1280, 1080)
            img.thumbnail(output_size)
            img.save(self.sliderImg.path)

class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
    orderQuantity = models.IntegerField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

class DeliveryStatus(models.Model):
    statusId = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20)

class Delivery(models.Model):
    deliveryId = models.AutoField(primary_key=True)
    productid = models.ForeignKey(Products, on_delete=models.CASCADE)
    status = models.ForeignKey(DeliveryStatus, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)