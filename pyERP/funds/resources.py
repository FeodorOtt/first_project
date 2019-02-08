from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from .models import Currency, Client, Transaction
from tastypie.authorization import Authorization


class ClientResource(ModelResource):
    responsible_client = fields.ForeignKey('self', 'responsible_client', null=True)
    class Meta:
        # allowed_methods = ['get']
        queryset = Client.objects.all().order_by('name')
        resource_name = 'client'
        authorization = Authorization()
        # filtering = {
        #     'id': ALL_WITH_RELATIONS
        # }

    # def dehydrate_name(self, bundle):
    #     return bundle.data['responsible_client_id'].upper()


class TransactionResource(ModelResource):
    currency = fields.ForeignKey('funds.resources.CurrencyResource', 'currency')
    db_client_id = fields.ForeignKey('funds.resources.ClientResource', 'db_client')
    cr_client_id = fields.ForeignKey('funds.resources.ClientResource', 'cr_client')
    class Meta:
        fields = ['id', 'oper_date', 'currency_rate', 'exchange_income', 'amount', 'amount_e', 'exchange_amount', 'exchange_amount_e',
            'payment_details', 'addinfo', 'status_id', 'handle_time', 'bankimport_id', 'cr_account_id', 'cr_client_id', 'currency_id',
            'db_account_id', 'db_client_id', 'exchange_currency_id', 'parent_id', 'partition_id', 'pattern_id', 'user_id'];
        queryset = Transaction.objects.all().order_by('id')
        resource_name = 'transaction'
        authorization = Authorization()


class CurrencyResource(ModelResource):
    # entry = fields.ToOneField('funds.resources.TransactionResourse', 'entry')
    class Meta:
        # fields = ['id', 'name']
        queryset = Currency.objects.all().order_by('name')
        resource_name = 'currency'
        authorization = Authorization()


