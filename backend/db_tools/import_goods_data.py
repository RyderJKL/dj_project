# -*- coding: utf-8 -*-

# 独立使用 django 的 model

import sys
import os

# 获取当前文件所在目录
pwd = os.path.dirname(os.path.relpath(__file__))
# 将整个根路径添加到 sys.path 中 (此种方式只是在运行时有效)
sys.path.append(pwd+"../")

# 以上操作指定了当前程序的运行目录是项目的根目录
# django model 依赖于 django 中的某些配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django
django.setup()

from goods.models import Goods, GoodsCategory, GoodsImages

from db_tools.data.product_data import row_data

for goods_detail in row_data:
  goods = Goods()
  goods.name = goods_detail["name"]
  goods.market_price = float(int(goods_detail["market_price"].replace("￥", "").replace("元", "")))
  goods.shope_price = float(int(goods_detail["sale_price"].replace("￥", "").replace("元", "")))
  goods.good_brief = goods_detail["desc"] if goods_detail["desc"] is not None else ""
  goods.good_desc = goods_detail["goods_desc"] if goods_detail["goods_desc"] is not None else ""
  goods.good_front_image = goods_detail["images"][0] if goods_detail["images"] is not None else ""

  category_name = goods_detail["categories"][-1]
  category = GoodsCategory.objects.filter(name=category_name)
  if category:
    goods.category = category[0]

  goods.save()

  for goods_image in goods_detail["images"]:
    goods_image_instance = GoodsImages()
    goods_image_instance.image = goods_image
    goods_image_instance.goods = goods
    goods_image_instance.save()

