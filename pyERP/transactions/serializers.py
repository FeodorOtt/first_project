from rest_framework import serializers
from .models import Transactions, Clients, Currency

class TransactionsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = ('db_client_id', 'cr_client_id', 'amount', 'currency_id', 'amount_e', 'payment_details')
        # fields = ('__all__')

class ClientsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Clients
        # fields = ('db_client_id', 'amount','payment_details')
        fields = ('__all__')

class CurrencySerializers(serializers.ModelSerializer):

    class Meta:
        model = Currency
        # fields = ('db_client_id', 'amount','payment_details')
        fields = ('__all__')
