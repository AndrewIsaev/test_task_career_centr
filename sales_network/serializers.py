from rest_framework import serializers

from sales_network.models import Unit


class SecondTierSupplier(serializers.ModelSerializer):
    """
    Second tier supplier serializer
    """

    type = serializers.SerializerMethodField()

    def get_type(self, obj: Unit) -> str:
        """Display unit type from choices"""
        return obj.get_type_display()

    class Meta:
        model = Unit
        fields = ['id', 'title', 'type']


class FirstTierSupplier(serializers.ModelSerializer):
    """
    First tier supplier serializer
    """

    supplier = SecondTierSupplier()
    type = serializers.SerializerMethodField()

    def get_type(self, obj: Unit) -> str:
        """Display unit type from choices"""
        return obj.get_type_display()

    class Meta:
        model = Unit
        fields = [
            'id',
            'title',
            'type',
            'supplier',
        ]


class UnitSerializer(serializers.ModelSerializer):
    """
    Unit serializer
    """

    supplier = FirstTierSupplier(read_only=True)
    type = serializers.SerializerMethodField()

    def get_type(self, obj: Unit) -> str:
        """Display unit type from choices"""
        return obj.get_type_display()

    class Meta:
        model = Unit
        fields = '__all__'


class UnitCreateSerializer(serializers.ModelSerializer):
    """Unit create update serializer"""

    supplier = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())

    class Meta:
        model = Unit
        fields = ['title', 'type', 'debt', 'supplier', 'contact', 'product']
        read_only_fields: list[str] = ['debt']
