from rest_framework import viewsets
from ..models import Digit
from .serializers import DigitalSerializer

class DigitViewSet(viewsets.ModelViewSet):
    serializer_class = DigitalSerializer
    queryset = Digit.objects.all()