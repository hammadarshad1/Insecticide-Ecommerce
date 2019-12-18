from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Products)
admin.site.register(models.Category)
admin.site.register(models.Cart)
admin.site.register(models.DeliveryStatus)
admin.site.register(models.SliderImage)
admin.site.register(models.Comments)
admin.site.register(models.Order)