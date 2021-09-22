
from django.urls import path
from blog.views import post_view,post_details,delete_view,edit_view



urlpatterns =[
    path('',post_view,name="post"),
    path('post-detail/<int:id>/',post_details,name="post-detail"),
    path('delete-post/<int:id>/',delete_view,name="post-delete"),
    path('edit-post/<int:id>/',edit_view,name='post-edit'),
]