from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Games
from .serializers import GameReadSerializer, GameWriteSerializer

# Create your views here.

# ViewSet para manejar games
class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()

    # Serializador según la acción
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return GameWriteSerializer
        return GameReadSerializer # Serializador de lectura