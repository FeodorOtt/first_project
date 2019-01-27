from rest_framework import serializers
from .models import Transactions, Clients

class TransactionsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = ('db_client_id', 'amount','payment_details')
        # fields = ('__all__')

class ClientsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Clients
        # fields = ('db_client_id', 'amount','payment_details')
        fields = ('__all__')
