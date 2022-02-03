from rest_framework import generics
from .serializers import ShopSerializer, DonutSerializer
from .models import Shop, Donut

# Create your views here.


class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class DonutList(generics.ListCreateAPIView):
    queryset = Donut.objects.all()
    serializer_class = DonutSerializer


class DonutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donut.objects.all()
    serializer_class = DonutSerializer
