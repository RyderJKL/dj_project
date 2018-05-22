from rest_framework import routers
# from article.viewsets import ArticleViewSet
from goods.viewsets import GoodsListViewSet

router = routers.DefaultRouter()
# router.register(r'article', ArticleViewSet, base_name='article')
router.register(r'good', GoodsListViewSet, base_name='good')
