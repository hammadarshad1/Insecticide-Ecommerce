from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Gender(models.Model):
    genderId = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender
        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cnic = models.CharField(max_length=15)
    phoneNo = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    # parent_id = models.IntegerField()
    dateOfBirth = models.DateField(null = True, blank=True)
    img = models.ImageField(default='default.jpg', upload_to='users')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.img.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.img.path)