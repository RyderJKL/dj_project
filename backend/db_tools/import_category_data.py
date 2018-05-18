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

from goods.models import GoodsCategory

from db_tools.data.category_data import  row_data

props = {
  'code': 'code',
  'name': 'name',
  'sub_categories': 'sub_categories'
}

for leve1_cat in row_data:
    leve1_instance = GoodsCategory()
    leve1_instance.code = leve1_cat[props['code']]
    leve1_instance.name = leve1_cat[props['name']]
    leve1_instance.category_type = 1
    leve1_instance.save()

    for leve2_cat in leve1_cat[props['sub_categories']]:
      leve2_instance = GoodsCategory()
      leve2_instance.code = leve2_cat[props['code']]
      leve2_instance.name = leve2_cat[props['name']]
      leve2_instance.category_type = 2
      leve2_instance.parent_category = leve1_instance
      leve2_instance.save()

      for leve3_cat in leve2_cat[props['sub_categories']]:
        leve3_instance = GoodsCategory()
        leve3_instance.code = leve3_cat[props['code']]
        leve3_instance.name = leve3_cat[props['name']]
        leve3_instance.category_type = 3
        leve3_instance.parent_category = leve2_instance
        leve3_instance.save()

