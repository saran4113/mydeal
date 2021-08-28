

from rest_framework import serializers
from .models import MyDeal

class MyDealSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyDeal
        fields = ('__all__')
