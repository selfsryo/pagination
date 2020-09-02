from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
	# 関数ビュー
    path('', views.index, name='index'),

	# クラスベースビュー
    # path('', views.IndexView.as_view(), name='index'),

	# DRF
	# path('api/posts/', views.PostListView.as_view(), name='index'),
]
