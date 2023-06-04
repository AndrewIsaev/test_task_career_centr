from rest_framework import serializers

from sales_network.models import Unit


class SecondTierSupplier(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    readonly_fields = ['debt']

    def get_type(self, obj):
        return obj.get_type_display()

    class Meta:
        model = Unit
        fields = ['id', 'title', 'type']


class FirstTierSupplier(serializers.ModelSerializer):
    supplier = SecondTierSupplier()
    type = serializers.SerializerMethodField()
    readonly_fields = ['debt']

    def get_type(self, obj):
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
    supplier = FirstTierSupplier()
    type = serializers.SerializerMethodField()
    readonly_fields = ['debt']

    def get_type(self, obj):
        return obj.get_type_display()

    class Meta:
        model = Unit
        fields = [
            'id',
            'title',
            'type',
            'supplier',
        ]
