from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogList, name='blog-list'),
    path('blog/<int:pk>', views.blogDetail, name='blog-detail'),
    path('bloggers/', views.bloggersList, name='bloggers-list'),
    path('blogger/<int:bloggerId>', views.bloggerDetail, name='blogger-details'),

]
