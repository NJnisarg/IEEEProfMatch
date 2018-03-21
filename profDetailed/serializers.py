from profDetailed.models import profDetailed
from rest_framework import serializers

class profDetailedSerializer(serializers.ModelSerializer):
	class Meta:
		model = profDetailed
		fields = '__all__'