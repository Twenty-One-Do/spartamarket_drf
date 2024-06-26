from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

urlpatterns = [
    # Auth
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('refresh/blacklist/', TokenBlacklistView.as_view()),

    # AccountsCRUD
    path('', views.Accounts.as_view()),
    path('<int:who>', views.Accounts.as_view()),
    path('password/', views.password_change),
    # Follow
    path('follow/', views.Follow.as_view()),
]

