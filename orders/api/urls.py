from django.urls import path
from orders.api.views import  OrderCreateListView
# from orders.api.views import  HelloOrdersView

urlpatterns = [
    # path('', HelloOrdersView.as_view(), name='hello-orders'),
    path('', OrderCreateListView.as_view() , name='orders')
]
