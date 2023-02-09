from django.urls import path
from .views import HelloOrdersView

urlpatterns = [
    path('', HelloOrdersView.as_view(), name='hello-orders')
]
