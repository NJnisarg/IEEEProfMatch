from rest_framework import serializers
from studentDetailed.models import studentDetailed

class studentDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentDetailed
        fields = '__all__'