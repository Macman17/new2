from django.urls import path
from articles import views


urlpatterns = [
    path('news/', views.NewsArticleListView.as_view(), name='news_list'),
    path('sports/', views.SportsArticleListView.as_view(), name='sports_list'),
    path('politics/', views.PoliticsArticleListView.as_view(), name='politics_list'),
    path('gogamecocks/', views.GoGamecocksArticleListView.as_view(), name='gogamecocks_list'),
    path('personalfinance/', views.PersonalFinanceArticleListView.as_view(), name='personalfinance_list'),
    path('new/', views.ArticleCreateView.as_view(), name='new'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.ArticleDeleteView.as_view(), name='delete'),
]
