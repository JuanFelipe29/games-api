from django.db import models

# Create your models here.
class Games(models.Model):
    title = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    platform = models.CharField(max_length=100)
    release_date = models.DateField()
    developer = models.CharField(max_length=200)
    description = models.TextField(null=True)
    rating = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='games/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title