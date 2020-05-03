from django.contrib import admin
from .models import Star,Order



@admin.register(Star)

class StarAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'available', 'price', 'subscribers')
    list_filter = ('available', 'price', 'subscribers')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = (
        'name',
        'nickname',
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'myName', 'reason', 'description', 'email', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']


