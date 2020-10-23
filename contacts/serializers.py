from rest_framework import serializers
from .models import Contact


class ContactsSerializer(serializers.ModelSerializer):
    role_json = serializers.ReadOnlyField(source='load_role', default=[])

    class Meta:
        model = Contact
        fields = '__all__'
