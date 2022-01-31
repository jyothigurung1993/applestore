from django.db import models

# Create your models here.

class GenresDetails(models.Model):
    name = models.CharField(max_length=200, blank=False)

    class Meta:
        db_table = "genres"

    def __str__(self):
        return self.name

class ProductDetails(models.Model):
    app_name = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    genres = models.ManyToManyField(GenresDetails)
    version = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    class Meta:
        db_table = "product_details"

    def __str__(self):
        return self.app_name+str(self.price)


