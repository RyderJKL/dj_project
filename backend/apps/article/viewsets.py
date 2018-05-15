from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer

  # return Response([queryset], status=status.HTTP_201_CREATED)
