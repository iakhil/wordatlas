from rest_framework import serializers 
from .models import UserPlay

class UserPlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlay
        fields = ['id', 'name', 'word', 'meaning']

        