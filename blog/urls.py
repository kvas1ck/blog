from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home,name = 'home'),
    path('about/', views.about, name = 'about'),
    path('posts/<slug:slug>/',views.post_detail, name = 'post_detail'),

    path('categories/<slug:slug>/',views.category_posts, name = 'category_posts'),

    path('tags/<slug:slug>/',views.tag_posts, name= 'tag_posts')
]

