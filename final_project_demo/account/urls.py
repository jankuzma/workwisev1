
from django.urls import path

from account.views import LoginUserView, UserProfileView, LogoutUserView, RegisterEmployerView, RegisterJobSeekerView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='user_login'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', LogoutUserView.as_view(), name='user_logout'),
    path('register/employer/', RegisterEmployerView.as_view(), name='employer_register'),
    path('register/jobseeker/', RegisterJobSeekerView.as_view(), name='jobseeker_register')
]
