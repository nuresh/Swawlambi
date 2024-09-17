from django.db import models
from autoslug import AutoSlugField 

class Slider(models.Model):
    caption = models.CharField(max_length=300, null=True)
    image = models.FileField(upload_to="slider", default=None)
    image_order = models.IntegerField()
    enabled = models.BooleanField(null=True)
    
    def __str__(self):
        return self.caption

    class Meta:
        db_table = 'sliders'
        verbose_name_plural = 'sliders'

class Product(models.Model):
    name = models.CharField(max_length=300, null=True)
    code = AutoSlugField(populate_from='name', unique=True,null=True,default=None)
    size = models.CharField(max_length=300, null=True)
    desc = models.TextField(null=True,blank=True)
    price = models.IntegerField()
    image = models.FileField(upload_to="slider", default=None)
    date_of_upload = models.DateField(null=True,blank=True)
   
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name_plural = 'products'

