from django.urls import path
from knox import views as knox_views
from users.views import get_user_data ,login_api,register

urlpatterns = [
    path('user/', get_user_data),
    path('login/', login_api),
    path('register/', register),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall')
]