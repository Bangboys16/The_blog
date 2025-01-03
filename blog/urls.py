from django.urls import path
from . views import Index, DetailArticleView, LikePost, Featured, BlogPostDeleteView
from . import views


urlpatterns = [
   path('', Index.as_view(), name='index'),
   path('<int:pk>/', DetailArticleView.as_view(), name='detail_post'),
   path('<int:pk>/like', LikePost.as_view(), name='like_post'),
   path('featured/', Featured.as_view(), name='featured'),
   path('<int:pk>/delete', BlogPostDeleteView.as_view(), name='delete_post'),
   path('create-blog/', views.create_blog_post, name='create-blog' ),
   path('update-blog/<int:id>/', views.task_update, name='update-blog'),
]
