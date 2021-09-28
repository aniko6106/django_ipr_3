from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Article, Author
from .serializers import (
    ArticleSerializer,
    AuthorNestedSerializer,
    AuthorSlugSerializer,
    AuthorStringSerializer,
    AuthorPrimaryKeySerializer,
    AuthorHyperlinkedSerializer,
)


class ArticleView(viewsets.ViewSet):
    """
    A simple ViewSet that for listing or retrieving users.
    """

    def list(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(user)
        return Response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class AuthorStringViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorStringSerializer
    queryset = Author.objects.all()


class AuthorPrimaryKeyViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorPrimaryKeySerializer
    queryset = Author.objects.all()


class AuthorHyperlinkedViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorHyperlinkedSerializer
    queryset = Author.objects.all()


class AuthorSlugViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSlugSerializer
    queryset = Author.objects.all()


class AuthorNestedViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorNestedSerializer
    queryset = Author.objects.all()
