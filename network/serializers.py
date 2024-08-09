from rest_framework import serializers

from network.models import Network


class NetworkSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Network.
    """
    class Meta:
        model = Network
        fields = "__all__"
        read_only_fields = ("debt",)  # 'debt' доступно только для чтения, что предотвращает его изменение через API.
