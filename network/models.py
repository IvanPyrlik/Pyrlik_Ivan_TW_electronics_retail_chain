from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Network(models.Model):
    """
    Модель Cети по продаже электроники.
    """
    FACTORY = 0
    NETWORK = 1
    ENTREPRENEUR = 2
    NETWORK_LINKS = [
        (FACTORY, "Завод"),
        (NETWORK, "Розничная сеть"),
        (ENTREPRENEUR, "Индивидуальный предприниматель"),
    ]

    name = models.CharField(max_length=200, verbose_name='Название')
    network_link = models.IntegerField(choices=NETWORK_LINKS, verbose_name='Звено сети')
    email = models.EmailField(verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=20, verbose_name='Номер дома')
    provider = models.ForeignKey("self", on_delete=models.SET_NULL,
                                 **NULLABLE, verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2,
                               verbose_name='Задолженность перед поставщиком')
    time_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сеть'
        verbose_name_plural = 'Сети'

    @property
    def get_level_network(self):
        """
        Функция для получения уровня сети.
        """
        # Завод всегда находится на 0 уровне
        if self.network_link == self.FACTORY:
            return 0

        # Если поставщик не указан, считаем уровень максимальным
        if not self.provider:
            return max(self.NETWORK, self.ENTREPRENEUR)

        # В противном случае определяем уровень на основе поставщика
        return self.get_level_network + 1


class Product(models.Model):
    """
    Модель Продукта.
    """
    name = models.CharField(max_length=200, verbose_name='Название')
    model = models.CharField(max_length=200, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')
    network = models.ForeignKey(Network, on_delete=models.CASCADE,
                                verbose_name='Сеть, продающая продукт')

    def __str__(self):
        return f"{self.name} - {self.model}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
