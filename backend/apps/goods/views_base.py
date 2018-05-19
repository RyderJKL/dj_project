from django.shortcuts import render
from django.views.generic.base import View
from goods.models import Goods
# Create your views here.

class GoodsListView(View):
  def get(self, request):
    json_list = []
    goods = Goods.objects.all()[:10]
    # version 1.0
    # for good in goods:
    #   json_dict = {}
    #   json_dict['name'] = good.name
    #   json_dict['category'] = good.category.name
    #   json_dict['market_price'] = good.market_price
     # json_list.append(json_dict)

    # version 2.0
    # from django.forms.models import model_to_dict
    # for good in goods:
    #   json_dict = model_to_dict(good)
    #   json_list.append(json_dict)

    # version 3.0
    # import json
    # from django.core import serializers
    # json_data = serializers.serialize('json', goods)
    # json_list = json.loads(json_data)

    # from django.http import JsonResponse
    # return JsonResponse(json_list, safe=False)

