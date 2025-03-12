from django.urls import path
from .views import get_posts, create_post, update_post, delete_post
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # Rutas usando FBV
    path('posts/', get_posts, name='get_posts'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:post_id>/update/', update_post, name='update_post'),
    path('posts/<int:post_id>/delete/', delete_post, name='delete_post'),

    # Rutas usando CBV
    path('cbv/posts/', PostListView.as_view(), name='post_list'),
    path('cbv/posts/create/', PostCreateView.as_view(), name='post_create'),
    path('cbv/posts/<int:post_id>/update/', PostUpdateView.as_view(), name='post_update'),
    path('cbv/posts/<int:post_id>/delete/', PostDeleteView.as_view(), name='post_delete'),
]