from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(User_Detail)
admin.site.register(Department)
admin.site.register(Product)
# admin.site.register(Shop_Details)
admin.site.register(Color_filter)
admin.site.register(Size_filter)
admin.site.register(Cart)
admin.site.register(Billingdetail)
admin.site.register(Order)
admin.site.register(Wishlist)