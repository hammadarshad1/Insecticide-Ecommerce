from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

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
    productRatings = models.FloatField()
    productSales = models.IntegerField()
    marketPrice = models.FloatField()
    discountedPrice = models.FloatField()
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.productTitle

    # def save(self):
    #     #Opening the uploaded image
    #     im = Image.open(self.productImg)

    #     output = BytesIO()

    #     #Resize/modify the image
    #     im = im.resize( (300,300) )

    #     #after modifications, save it to the output
    #     im.save(output, format='JPEG', quality=100)
    #     output.seek(0)

    #     #change the imagefield value to be the newley modifed image value
    #     self.productImg = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.productImg.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

    #     super(Products,self).save()
    def save(self):
        super().save()

        img = Image.open(self.productImg.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.productImg.path)

# class Comments(models.Model):
#     commentId = models.AutoField(primary_key=True)
#     commentText = models.TextField()
#     productId = models.ForeignKey(Products, on_delete=models.CASCADE)

# class Cart(models.Model):
#     cartId = models.AutoField(primary_key=True)
#     productId = models.ForeignKey(Products, on_delete=models.CASCADE)