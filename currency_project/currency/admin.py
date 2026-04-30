from django.contrib import admin
from .models import Currency

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'buy_rate', 'sell_rate', 'date')
    list_filter = ('date',)
    search_fields = ('name',)
    ordering = ('-date',)
