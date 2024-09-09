from django.urls  import url
from blog import views

urlpatterns = [
    url('', views.PostListView.as_view(), name='post_list'),
    url('about/', views.AboutView.as_view(), name='about'),
    url('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    url('post/new/', views.CreatePostView.as_view(), name='post_new'),
    url('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    url('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    url('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),    
    url('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    url('comment/<int:pk>/comment/approve/', views.comment_approve, name='comment_approve'),
    url('comment/<int:pk>/comment/remove/', views.comment_remove, name='comment_remove'),
     url('post/<int:pk>/publish/', views.post_publish, name='post_publish'),

]