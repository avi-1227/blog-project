from django.urls import path
from . import views

app_name = 'blogapp'


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
]