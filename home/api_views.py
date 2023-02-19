from .models import *
from .serializers import *
from rest_framework import viewsets
# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


import django_filters.rest_framework
from rest_framework import generics
from rest_framework import filters


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['category', 'subcategory','brand','status','labels']
    search_fields = ['name','description']
    ordering_fields = ['id','price','discounted_price']
