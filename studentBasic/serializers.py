from studentBasic.models import studentBasic
from rest_framework import serializers

class studentBasicSerializer(serializers.ModelSerializer):
	class Meta:
		model = studentBasic
		fields = ('username','firstName','lastName','state','city','gender','age','mobileNo')