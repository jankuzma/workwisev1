
from django.urls import path

from account.views import LoginUserView, UserProfileView, LogoutUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='user_login'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', LogoutUserView.as_view(), name='user_logout'),
]
