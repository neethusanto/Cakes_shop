from django.db import models

# Create your models here.

class Cake(models.Model):
    cake_name=models.CharField(max_length=250)
    cake_flavour=models.CharField(max_length=250)
    cake_desc=models.TextField()
    cake_price=models.IntegerField()
    cake_img=models.ImageField(upload_to='cake-imges')


    def __str__(self):
        return self.cake_name
