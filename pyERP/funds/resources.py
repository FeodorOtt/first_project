from tastypie.resources import ModelResource, ALL
from tastypie.authentication import BasicAuthentication
from tastypie import fields
from .models import Currency, Client, Transaction, User, Partition, ClientType, ClientTypeLocale, ClientCategory, Bank, Country
from tastypie.authorization import Authorization
from tastypie.constants import ALL
# from django.contrib.auth.models import User


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        # excludes = ['email', 'password', 'is_superuser']
        # Add it here.
        # authentication = BasicAuthentication()
        authorization = Authorization()

class ClientTypeResource(ModelResource):
    class Meta:
        queryset = ClientType.objects.all().order_by('name')
        # queryset=ClientType.objects.select_related('ClientTypeLocale').all()
        resource_name = 'clienttype'
        authorization = Authorization()

class ClientTypeLocaleResource(ModelResource):
    client_type_id = fields.ForeignKey('funds.resources.ClientTypeResource', 'client_type', null=True)
    class Meta:
        queryset = ClientTypeLocale.objects.select_related('client_type').all()
        resource_name = 'clienttypelocale'
        filtering = {
            'locale': ALL,
        }
        authorization = Authorization()

class ClientCategoryResource(ModelResource):
    class Meta:
        queryset = ClientCategory.objects.all().order_by('name')
        resource_name = 'clientcategory'
        authorization = Authorization()

class PartitionResource(ModelResource):
    # entry = fields.ToOneField('funds.resources.TransactionResourse', 'entry')
    class Meta:
        # fields = ['id', 'name']
        queryset = Partition.objects.all().order_by('name')
        resource_name = 'partition'
        authorization = Authorization()

class CountryResource(ModelResource):
    class Meta:
        limit = 0
        max_limit = 0
        # fields = ['id', 'name']
        queryset = Country.objects.all().order_by('name')
        resource_name = 'country'
        authorization = Authorization()


class BankResource(ModelResource):
    country_id = fields.ForeignKey('funds.resources.CountryResource', 'country', null=True)
    user_id = fields.ForeignKey('funds.resources.UserResource', 'user', null=True)
    class Meta:
        limit = 0
        max_limit = 0
        # fields = ['id', 'name']
        queryset = Bank.objects.all().order_by('name')
        resource_name = 'bank'
        authorization = Authorization()

class ClientResource(ModelResource):
    responsible_client = fields.ForeignKey('self', 'responsible_client', null=True)
    attracted_by = fields.ForeignKey('self', 'attracted_by', null=True)

    type_id = fields.ForeignKey('funds.resources.ClientTypeResource', 'type')
    category_id = fields.ForeignKey('funds.resources.ClientCategoryResource', 'category', null=True)
    user_id = fields.ForeignKey('funds.resources.UserResource', 'user', null=True)
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
    partition_id = fields.ForeignKey('funds.resources.PartitionResource', 'partition')
    currency_id = fields.ForeignKey('funds.resources.CurrencyResource', 'currency')
    db_client_id = fields.ForeignKey('funds.resources.ClientResource', 'db_client')
    cr_client_id = fields.ForeignKey('funds.resources.ClientResource', 'cr_client')
    user_id = fields.ForeignKey('funds.resources.UserResource', 'user', null=True)
    class Meta:
        limit = 0
        max_limit = 0
        fields = ['id', 'oper_date', 'currency_rate', 'exchange_income', 'amount', 'amount_e', 'exchange_amount', 'exchange_amount_e',
            'payment_details', 'addinfo', 'status_id', 'handle_time', 'bankimport_id', 'cr_account_id', 'cr_client_id', 'currency_id',
            'db_account_id', 'db_client_id', 'exchange_currency_id', 'parent_id', 'partition_id', 'pattern_id', 'user_id'];
        queryset = Transaction.objects.all().order_by('id')
        resource_name = 'transaction'
        filtering = {
            'oper_date': ALL,
            'amount': ALL
        }
        authorization = Authorization()

class CurrencyResource(ModelResource):
    # entry = fields.ToOneField('funds.resources.TransactionResourse', 'entry')
    class Meta:
        # fields = ['id', 'name']
        queryset = Currency.objects.all().order_by('name')
        resource_name = 'currency'
        authorization = Authorization()


