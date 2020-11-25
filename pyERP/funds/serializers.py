from rest_framework import serializers
from .models import Transaction, Client#, Currency
from tastypie.serializers import Serializer

# class TransactionSerializers(serializers.ModelSerializer):
#
#     class Meta:
#         model = Transaction
#         fields = ('db_client_id', 'cr_client_id', 'amount', 'currency_id', 'amount_e', 'payment_details')
#         # fields = ('__all__')
#
# class ClientSerializers(serializers.ModelSerializer):
#
#     class Meta:
#         model = Client
#         # fields = ('db_client_id', 'amount','payment_details')
#         fields = ('__all__')

# class CurrencySerializers(serializers.ModelSerializer):
#
#     class Meta:
#         model = Currency
#         # fields = ('db_client_id', 'amount','payment_details')
#         fields = ('__all__')
