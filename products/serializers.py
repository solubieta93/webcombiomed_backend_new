from rest_framework import serializers
from .models import Product, ProductType


# Serializers define the API representation.
class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    type = serializers.ReadOnlyField(source='typeId.title', default=None)

    class Meta:
        model = Product
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'
