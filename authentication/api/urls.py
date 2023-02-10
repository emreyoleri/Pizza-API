from django.urls import path
from .views import HelloAuthView , UserCreateView

urlpatterns = [
    path('', HelloAuthView.as_view(), name='hello_auth'),
    path('signup/' , UserCreateView.as_view(), name='sign_up')
]
