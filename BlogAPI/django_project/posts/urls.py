from django.urls import path

from .views import PostList, PostDetail,UserDetail,UserList

urlpatterns = [
    path("users/", UserList.as_view()),  
    path("users/pk>/", UserDetail.as_view()),
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
]