

from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.post_list ),
    path('posts/<int:id>/', views.post_detail ),
    path('category/<int:pk>/', views.category_detail, name='category-detail' ),
    path('comment/', views.CommentListCreateAPIView.as_view(), name='comment-list' ),
    path('comment/<int:pk>/', views.CommentDetailUpdateAPIView.as_view(), name='comment-detail' ),
    # path('comment/<int:pk>/update/', views.CommentUpdateAPIView.as_view(), name='comment-update' ),
]
