from rest_framework import serializers
from studentDetailed.models import studentDetailed


class studentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentDetailed
        fields = ('username', 'cgpa', 'institute')
