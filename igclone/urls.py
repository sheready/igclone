from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,LikeView,AddCommentView,PostDeleteView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',PostListView.as_view(), name = 'igclone-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/',PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
    path('like/<int:pk>/',LikeView, name='like_post'),
    path('post/<int:pk>/comment/',AddCommentView.as_view(),name = 'add_comment'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post-delete'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)