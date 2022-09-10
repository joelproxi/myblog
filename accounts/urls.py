

from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view' ),
    path('register/', views.register_view, name='register_view' ),
    
    path('dashboad/', views.dashboard, name='dashboad' ),
    path('edit/', views.editProfile, name='edit_profie' ),
]
