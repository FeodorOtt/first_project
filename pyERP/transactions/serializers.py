from rest_framework import serializers
from .models import Transactions

class TransactionsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = ('db_client_id', 'amount','payment_details')
        # fields = ('__all__')
