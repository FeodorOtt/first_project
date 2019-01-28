from django.contrib import admin

from .models import Transaction, Client, Currency

class CurrencyAdmin(admin.ModelAdmin):
    """
    Справочник валют
    """
    list_display = ('name', 'ISO_char')

class ClientAdmin(admin.ModelAdmin):
    """
    Справочник клиентов
    """
    list_display = ('name', 'text_id')

class TransactionAdmin(admin.ModelAdmin):
    """
    Журнал транзакций
    """
    list_display = ("db_client_id","amount","payment_details")

admin.site.register(Currency,CurrencyAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Transaction,TransactionAdmin)
