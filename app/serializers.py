from app.models import Tod

from rest_framework import serializers

class TodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tod
        fields = ['id', 'name', 'done', 'created_at']