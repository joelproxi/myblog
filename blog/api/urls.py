
from django.urls import path,include

from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers

from . import views


router = SimpleRouter()

router.register('posts', views.PostViewSet)

comment_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')

comment_router.register('comments', views.CommentViewSet, basename='post-comment')


# urlpatterns = [
#     path('posts/', views.post_list ),
#     path('posts/<int:id>/', views.post_detail ),
#     path('category/<int:pk>/', views.category_detail, name='category-detail' ),
#     path('comment/', views.CommentListCreateAPIView.as_view(), name='comment-list' ),
#     path('comment/<int:pk>/', views.CommentDetailUpdateAPIView.as_view(), name='comment-detail' ),
#     # path('comment/<int:pk>/update/', views.CommentUpdateAPIView.as_view(), name='comment-update' ),
# ]


urlpatterns = [
    path("", include(router.urls)),
    path("", include(comment_router.urls)),
]
