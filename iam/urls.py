from django.urls import path
from iam.views.auth_view import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login')
]