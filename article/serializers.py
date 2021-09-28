from rest_framework import serializers

from .models import Article, Author


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'body', 'author')


class AuthorStringSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'email', 'articles')


class AuthorPrimaryKeySerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'email', 'articles')


class AuthorHyperlinkedSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='articles-detail'
    )

    class Meta:
        model = Author
        fields = ('id', 'name', 'email', 'articles')


class AuthorSlugSerializer(serializers.ModelSerializer):
    articles = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Author
        fields = ('id', 'name', 'email', 'articles')


class AuthorNestedSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'email', 'articles')
