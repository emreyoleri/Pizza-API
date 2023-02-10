from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','flavour','size','order_status','size']
    list_filter=['placed_at','updated_at','order_status']


admin.site.register(Order,OrderAdmin)

