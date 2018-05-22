from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import viewsets
from .serializers import GoodsSerializer
from .models import Goods


class GoodsListPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'limit'
    page_query_param = 'page'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsListPagination
