from django.urls import path, include
from rest_framework.routers import DefaultRouter  # Importa DefaultRouter

from .views import GamesViewSet # Importa los ViewSets

router = DefaultRouter()  # Crea un enrutador por defecto
router.register(r'games', GamesViewSet, basename='games')

urlpatterns = [
    path('', include(router.urls)),  # Incluir las rutas del enrutador
]
