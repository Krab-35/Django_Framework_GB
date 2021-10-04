from django.urls import path

from users.views import LoginFormView, RegistrationCreateView, LogoutLogoutView, ProfileUpdateView, \
    verify, registration, profile

app_name = 'users'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    # path('registration/', RegistrationCreateView.as_view(), name='registration'),
    path('registration/', registration, name='registration'),
    path('logout/', LogoutLogoutView.as_view(), name='logout'),
    # path('profile/<int:pk>', ProfileUpdateView.as_view(), name='profile'),
    path('profile/', profile, name='profile'),
    path('verify/<str:email>/<str:activation_key>/', verify, name='verify'),
]
