from django.urls import path
from .views import home, profile, RegisterView

app_name = 'users_en'

urlpatterns = [
    path('', home, name='users-home_en'),
    path('register_en/', RegisterView.as_view(), name='users-register_en'),
    path('profile_en/', profile, name='users-profile_en'),
]
