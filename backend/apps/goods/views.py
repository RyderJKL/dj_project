# version 1.0
# from .serializers import GoodsSerializer
# from .models import Goods
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .serializers import GoodsSerializer
from .models import Goods

class GoodsListPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'limit'
    page_query_param = 'page'
    max_page_size = 100

class GoodsListView(generics.ListAPIView):
    # version 1.0
    # def get(self, request, format=None):
    #   goods = Goods.objects.all()[:10]
    #   goods_serializer = GoodsSerializer(goods, many=True)
    #   return Response(goods_serializer.data)
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsListPagination
