from tastypie.resources import ModelResource
from tastypie import fields
from .models import Currency, Client, Transaction
from tastypie.authorization import Authorization


class ClientResourse(ModelResource):
    responsible_client = fields.ForeignKey('self', 'client', null=True)
    class Meta:
        queryset = Client.objects.all()
        resource_name = 'client'
        authorization = Authorization()


class TransactionResourse(ModelResource):
    currency = fields.ForeignKey('funds.resources.CurrencyResource', 'currency')
    class Meta:
        # fields = ['id', 'currency_id']
        queryset = Transaction.objects.all()
        resource_name = 'transaction'
        authorization = Authorization()


class CurrencyResource(ModelResource):
    # entry = fields.ToOneField('funds.resources.TransactionResourse', 'entry')
    class Meta:
        # fields = ['id', 'name']
        queryset = Currency.objects.all()
        resource_name = 'currency'
        authorization = Authorization()


