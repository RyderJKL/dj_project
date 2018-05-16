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

from goods.models import Goods, GoodsCategory, GoodsImage

from db_tools.data.product_data import row_data

props = {
  code: 'code',
  name: 'name',
  sub_categorys: 'sub_categorys'
}
