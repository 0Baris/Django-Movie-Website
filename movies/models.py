from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    film_adi = models.CharField(max_length=200)
    aciklama = models.TextField()
    resim = models.ImageField(upload_to ='static/img/') 
    anasayfa = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.film_adi