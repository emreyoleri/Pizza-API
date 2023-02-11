from orders.models import Order
from rest_framework import serializers

class OrderCreationSerializer(serializers.ModelSerializer):
    size=serializers.CharField(max_length=20)
    order_status=serializers.HiddenField(default='PENDING')
    quantity=serializers.IntegerField()

    class Meta:
        model=Order
        fields=['id','size','order_status','quantity']