from rest_framework import serializers
from products.models import Product


# Serializers define the API representation.
class ProductSerializer(serializers.ModelSerializer):
    # The source argument controls which attribute is used to populate a field and can point at any attribute
    # on the serialized instance.
    owner = serializers.ReadOnlyField(source='owner.username')
    # We could have also used
    # owner = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'owner', 'name', 'description']

#   default implementations method
#   def create()
#   def update()
