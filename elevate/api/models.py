from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)


    def __str__(self):
        return self.name