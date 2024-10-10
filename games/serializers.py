from rest_framework import serializers
from .models import Games

"""
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
"""

# Serializador para operaciones de lectura
class GameReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['id', 'title', 'gender', 'platform', 'release_date', 'developer', 'description', 'rating', 'price', 'image', 'created_at', 'updated_at']

# Serializador para operaciones de escritura
class GameWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['title', 'gender', 'platform', 'release_date', 'developer', 'description', 'rating', 'price', 'image']