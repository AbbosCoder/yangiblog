from django.urls import path 
from .views import ArticleListView,ArticleUpdateView,ArticleDeleteView,ArticleDetailView, ArticleCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:pk>/edit/',ArticleUpdateView.as_view(),name='article_edit'),
    path('<int:pk>/',ArticleDetailView.as_view(),name='article_detail'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name='article_delete'),
    path('',ArticleListView.as_view(),name='article_list'),
    path('new/',ArticleCreateView.as_view(),name='article_new'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)