from rest_framework import viewsets, filters

from network.models import Network
from network.permissions import IsActiveEmployee
from network.serializers import NetworkSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Network.
    """
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActiveEmployee]  # Доступ только для активных сотрудников
    filter_backends = [filters.SearchFilter]  # Включаем возможность поиска
    search_fields = ["country"]  # Поля для поиска по 'стране'

    def perform_update(self, serializer):
        """
        Обрабатываем операцию обновления Network.
        """
        # Сохраняем объект, не позволяя изменять значение 'debt'
        serializer.save(debt=self.get_object().debt)
