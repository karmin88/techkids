from django.urls import path
from .views import home  # Import the 'home' view

from .import views

urlpatterns = [
    path('', home, name='home'),
    path('forum/', views.forum, name='forum'),
    
    path('forum/<str:tag>/', views.forum, name='forum_with_tag'),  # Add this line for forum with tag
    path('user-post/', views.userPost, name='user-post'),
    path('topic/<int:pk>/', views.postTopic, name='topic-detail'),
    path('search-result/', views.searchView, name='search-result'),
    path('user-dashboard/', views.userDashboard, name='user-dashboard'),
    path('upvote/', views.upvote, name='upvote'),
    path('downvote/', views.downvote, name='downvote'),
    path('blog/', views.blogListView, name='blog'),
    path('article/<slug:slug>/', views.blogDetailView, name='article-detail'),
]
