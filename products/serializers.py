from rest_framework import serializers
from .models import Product, ProductType


# Serializers define the API representation.
class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    type = serializers.ReadOnlyField(source='typeId.title', default=None)
    details = serializers.ReadOnlyField(source='load_details', default=[])
    files = serializers.ReadOnlyField(source='load_files', default=[])
    images = serializers.ReadOnlyField(source='load_images', default=[])

    class Meta:
        model = Product
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):
    title_json = serializers.ReadOnlyField(source='load_title', default=[])
    description_json = serializers.ReadOnlyField(source='load_description', default=[])

    class Meta:
        model = ProductType
        fields = '__all__'
