from django.contrib import admin

from .models import Transactions, Clients, Currency

class CurrencyAdmin(admin.ModelAdmin):
    """
    Справочник валют
    """
    list_display = ('name', 'ISO_char')

class ClientsAdmin(admin.ModelAdmin):
    """
    Справочник клиентов
    """
    list_display = ('name', 'text_id')

class TransactionsAdmin(admin.ModelAdmin):
    """
    Журнал транзакций
    """
    list_display = ("db_client_id","amount","payment_details")

admin.site.register(Currency,CurrencyAdmin)
admin.site.register(Clients,ClientsAdmin)
admin.site.register(Transactions,TransactionsAdmin)
