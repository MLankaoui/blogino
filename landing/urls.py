from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:category_id>/', views.category, name='category'),
    path('create_post/', views.create_post, name='create_post'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]
