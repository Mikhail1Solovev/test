from django.contrib import admin
from .models import NetworkNode, Product

@admin.action(description="Clear debt for selected nodes")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0.00)

@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'supplier', 'debt', 'created_at')
    list_filter = ('city',)
    search_fields = ('name', 'email')
    actions = [clear_debt]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'network_node')
    list_filter = ('release_date',)
    search_fields = ('name', 'model')
