from django.urls import path
from . import views


app_name = "blogapp"

urlpatterns = [
    # post views
    path("", views.post_list, name="post_list"),
    path("<slug:post>/", views.post_detail, name="post_detail"),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path("blog/search/", views.post_search, name='post_search'),
]
