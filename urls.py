from django.urls import path
from .views import home, profile, RegisterView, main, about, contact

urlpatterns = [
    path('user', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('', main, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
