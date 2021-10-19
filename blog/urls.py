
from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('category/<slug:category>/', views.post_list, name='category_post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug>/',
         views.post_detail, name='post_detail'),
    # path('', views.PostListView.as_view(), name='post_list'),
]
