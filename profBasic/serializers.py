from profBasic.models import profBasic
from rest_framework import serializers

class profBasicSerializer(serializers.ModelSerializer):
	class Meta:
		model = profBasic
		fields = ('username','firstName','lastName','state','city','gender','age','mobileNo','institute','department','areas','websiteLinks')