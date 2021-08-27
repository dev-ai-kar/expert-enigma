from rest_framework import serializers
from ..models import Digit

class DigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digit
        fields = ('id','image','result')