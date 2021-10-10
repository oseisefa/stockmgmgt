from django.contrib import admin
from .models import Stock
from .forms import StockCreateForm
from .models import *
# Register your models here.


class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['category', 'item_name', 'quantity']
   form = StockCreateForm
   list_filter = ['category']
   search_fields = ['category', 'item_name', 'quantity']

admin.site.register(Stock)
admin.site.register(Category)