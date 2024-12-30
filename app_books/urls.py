from django.urls import path

from .views import UserRegistrationView, UserLoginView, UserLogoutView, HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('registro/', UserRegistrationView.as_view(), name="registro"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
]
