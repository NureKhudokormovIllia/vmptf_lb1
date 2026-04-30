from django.shortcuts import render
from django.utils import timezone
from .models import Currency

def currency_list(request):
    currencies = Currency.objects.all()
    return render(request, 'currency/currency_list.html',
                  {'currencies': currencies})

def today_rates(request):
    today = timezone.now().date()
    currencies = Currency.objects.filter(date=today)
    return render(request, 'currency/today_rates.html',
                  {'currencies': currencies, 'today': today})
