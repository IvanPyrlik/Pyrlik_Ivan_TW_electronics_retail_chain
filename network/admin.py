from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from network.models import Network, Product


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    """
    Админ панель для модели Network.
    """
    list_display = (
        "name",
        "email",
        "country",
        "city",
        "provider_link",
        "debt",
        "time_creation",
    )
    list_filter = ("city",)
    search_fields = ("name", "city")
    actions = ["clear_debt"]

    def provider_link(self, obj):
        """
        Создаем ссылку поставщика.
        """
        if obj.provider:
            url = reverse("admin:network_change", args=[obj.provider.pk])
            return format_html('<a href="{}">{}</a>', url, obj.provider.name)
        return "-"

    provider_link.short_description = "Поставщик"

    def clear_debt(self, request, queryset):
        """
        Для очищения задолженности перед поставщиком.
        """
        queryset.update(debt=0)
        self.message_user(request, "Задолженность перед поставщиком успешно очищена у выбранных объектов.")

    clear_debt.short_description = "Очистить задолженность"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Админ панель для модели Product.
    """
    list_display = ("name", "model", "release_date", "network")
    list_filter = ("network",)
    search_fields = ("name", "model")
