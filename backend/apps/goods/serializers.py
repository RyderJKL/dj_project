from rest_framework import serializers
from goods.models import Goods, GoodsCategory

class GoodsCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = GoodsCategory
    fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
  # 通过 rest_framework 序列化嵌套实现外键关系
  category = GoodsCategorySerializer()
  class Meta:
    model = Goods
    # 通过 '__all__' 可以提过 models 中所有字段
    # fields = '__all__'
    fields = ('name', 'category', 'click_num', 'goods_front_image', 'market_price', 'add_time')
