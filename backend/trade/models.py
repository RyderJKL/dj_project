from datetime from datetime
from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class ShoppingCart(models.Model):
  """
  购物车
  """
  user = models.ForeignKey(
    User,
    verbose_name=u"用户"
  )

  goods = models.ForeignKey(
    Goods,
    verbose_name=u"商品"
  )

  nums = models.IntegerField(
    default=0,
    verbose_name="购买数量"
  )

  add_time = models.DateTimeField(
    default=datetime.now,
    verbose_name=u"添加时间"
  )

  class Meta:
    verbose_name="购物车"
    verbose_name_plural = verbose_name
    unique_together = ("user", "goods")

  def __str__(self):
    return "%s(%d)".format(self.goods.name, self.nums)


class OrderInfo(modes.Model):
  """
  订单
  """
  ORDER_STATUS = (
    ("SUCCESS", "成功"),
    ("CLOSED", "超时关闭"),
    ("WAIT_BUYER_PAY", "交易创建"),
    ("FINISHED", "交易结束"),
    ("PAYING", "")
  )
