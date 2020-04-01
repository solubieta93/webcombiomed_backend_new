from rest_framework import serializers
from chat.models import ChatSession, ChatSessionMember, ChatSessionMessage


class ChatSessionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ChatSession
        fields = ('owner', 'create_date', 'update_date', 'uri')
            # '__all__'


class ChatSessionMemberSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ChatSessionMember
        fields = '__all__'


class ChatSessionMessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ChatSessionMessage
        fields = '__all__'
