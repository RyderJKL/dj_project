# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
from .serializers import GoodsSerializer
from .models import Goods

from rest_framework.views import APIView

from rest_framework.response import Response

class GoodsListView(APIView):
  def get(self, request, format=None):
    goods = Goods.objects.all()[:10]
    goods_serializer = GoodsSerializer(goods, many=True)
    return Response(goods_serializer.data)


