from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ArticleView,
    ArticleViewSet,
    AuthorHyperlinkedViewSet,
    AuthorNestedViewSet,
    AuthorStringViewSet,
    AuthorPrimaryKeyViewSet,
    AuthorSlugViewSet,
)


api_router = DefaultRouter()
# по данным ссылкам приведены примеры всех видов сериалайзеров из документации DRF
api_router.register(r'articles', ArticleViewSet, basename='articles')
api_router.register(r'authors-string', AuthorStringViewSet, basename='authors_string')
api_router.register(r'authors-prkey', AuthorPrimaryKeyViewSet, basename='authors_prkey')
api_router.register(
    r'authors-hyperlinked', AuthorHyperlinkedViewSet, basename='authors_hyperlinked'
)
api_router.register(r'authors-slug', AuthorSlugViewSet, basename='authors_slug')
api_router.register(r'authors-nested', AuthorNestedViewSet, basename='authors_nested')
# данные ссылки относятся к уроку часть 3
urlpatterns = [
    path('articles-view/', ArticleView.as_view({'get': 'list'})),
    path('articles-view/<int:pk>', ArticleView.as_view({'get': 'retrieve'})),
]


urlpatterns += api_router.urls
