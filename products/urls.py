from django.urls import path
from . import views

urlpatterns = [
    # products
    path('', views.ProductList.as_view()),
    path('<int:what>', views.Products.as_view()),
    # Comments
    path('<int:what>/comments/', views.Comments.as_view()),
    path('comments/<int:comment_id>', views.Comments.as_view()),
    # Likes
    path('likes/', views.Likes.as_view()),
]