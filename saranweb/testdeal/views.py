from django.shortcuts import render
from .models import MyDeal
from rest_framework import viewsets
from .serializers import MyDealSerializers

# Create your views here.
def index(request):
    myDeals = MyDeal.objects.all().order_by("-enroll")
    return render(request,"index.html",{"myDeals":myDeals})


class MyDealViewSet(viewsets.ModelViewSet):
    queryset = MyDeal.objects.all()
    serializer_class = MyDealSerializers