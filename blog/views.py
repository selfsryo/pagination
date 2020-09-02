from .models import Post

# 関数ビュー
from django.shortcuts import render
from django.core.paginator import Paginator

def index(request):
    # 各ページ2記事ずつ表示
    paginator = Paginator(Post.objects.all(), 2)
    # URLのクエリパラメータから現在のページ数を取得
    current_page_number = request.GET.get('page')
    # 現在のページのインスタンスを取得
    current_page_posts = paginator.get_page(current_page_number)
    # テンプレートに渡す
    return render(request, 'blog/index.html', {'post_list': current_page_posts})



# クラスベースビュー
# from django.views import generic

# class IndexView(generic.ListView):
# 	model = Post
# 	paginate_by = 2
# 	template_name = 'blog/index.html'



# DRF
# from rest_framework import generics, pagination, response
# from .serializers import PostSerializer

# class CustomPagination(pagination.CursorPagination):
# 	page_size = 2
# 	ordering = ('id',)

# 	def get_paginated_response(self, data):
# 		return response.Response({
# 			'next': self.get_next_link(),
# 			'previous': self.get_previous_link(),
# 			'page_size': self.page_size,
# 			'results': data
# 		})

# class PostListView(generics.ListAPIView):
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer
# 	pagination_class = CustomPagination
