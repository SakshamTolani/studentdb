from django.urls import path,include
from . import views

#urls for apis
urlpatterns = [
    #api for users to login
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    #api for students or teachers to see their profile
    path('users/profile/', views.getUserProfile, name='user-profile'),
    #api for admin to see the list of users.
    path('users/', views.getUsers, name='users'),
    #api for admin to add a new student
    path('users/register/', views.registerUser, name='user-register'),
    #api to reset password
    path('users/reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]