from tastypie.resources import ModelResource, ALL
from tastypie.authentication import BasicAuthentication
from tastypie import fields
from .models import Currency, Client, Transaction, TransactionDetail, User, Partition, ClientType, ClientTypeLocale, \
    ClientCategory, ClientCategoryLocale, Bank, Country, AccountType, AccountTypeLocale, AccountCategory, AccountCategoryLocale, Account, \
    BalanceAccount, AccountSaldoType, AccountPartition
from tastypie.authorization import Authorization
from tastypie.constants import ALL
from django.db.models import Q
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

class ClientCategoryLocaleResource(ModelResource):
    client_category_id = fields.ForeignKey('funds.resources.ClientCategoryResource', 'client_category', null=True)
    class Meta:
        queryset = ClientCategoryLocale.objects.select_related('client_category').all()
        resource_name = 'clientcategorylocale'
        filtering = {
            'locale': ALL,
        }
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
        limit = 0
        max_limit = 0
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
        queryset = Transaction.objects.all().order_by('-id')
        resource_name = 'transaction'
        filtering = {
            'oper_date': ALL,
            'db_client_id': ALL,
            'cr_client_id': ALL,
        }
        authorization = Authorization()

class TransactionDetailResource(ModelResource):
    transaction_id = fields.ForeignKey('funds.resources.TransactionResource', 'transaction')
    partition_id = fields.ForeignKey('funds.resources.PartitionResource', 'partition')
    currency_id = fields.ForeignKey('funds.resources.CurrencyResource', 'currency')
    db_client_id = fields.ForeignKey('funds.resources.ClientResource', 'db_client')
    db_account_id = fields.ForeignKey('funds.resources.AccountResource', 'db_account')
    cr_client_id = fields.ForeignKey('funds.resources.ClientResource', 'cr_client')
    cr_account_id = fields.ForeignKey('funds.resources.AccountResource', 'cr_account')
    user_id = fields.ForeignKey('funds.resources.UserResource', 'user', null=True)

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}
        orm_filters = super(TransactionDetailResource, self).build_filters(filters)

        if 'query' in filters:
            query = filters['query']
            qset = (
                    Q(db_account_id=query) |
                    Q(cr_account_id=query)
                    )
            orm_filters.update({None: qset}) # None is used as the key to specify that these are non-keyword filters

        return orm_filters

    def apply_filters(self, request, applicable_filters):
        return self.get_object_list(request).filter(*applicable_filters.pop(None, []), **applicable_filters)
        # Taking the non-keyword filters out of applicable_filters (if any) and applying them as positional arguments to filter()

    class Meta:
        limit = 0
        max_limit = 0
        # fields = ['id', 'oper_date', 'currency_rate', 'exchange_income', 'amount', 'amount_e', 'exchange_amount', 'exchange_amount_e',
        #     'payment_details', 'addinfo', 'status_id', 'handle_time', 'bankimport_id', 'cr_account_id', 'cr_client_id', 'currency_id',
        #     'db_account_id', 'db_client_id', 'exchange_currency_id', 'parent_id', 'partition_id', 'pattern_id', 'user_id'];
        queryset = TransactionDetail.objects.all()#.order_by('-id')
        resource_name = 'transactiondetail'
        filtering = {
            'transaction_id': ALL,
            'db_account_id': ALL,
            'cr_account_id': ALL,
            # 'query': ALL,
        }
        authorization = Authorization()

class CurrencyResource(ModelResource):
    # entry = fields.ToOneField('funds.resources.TransactionResourse', 'entry')
    class Meta:
        # fields = ['id', 'name']
        queryset = Currency.objects.all().order_by('name')
        resource_name = 'currency'
        authorization = Authorization()

class AccountTypeResource(ModelResource):
    class Meta:
        queryset = AccountType.objects.all()
        resource_name = 'accounttype'
        authorization = Authorization()

class AccountTypeLocaleResource(ModelResource):
    account_type_id = fields.ForeignKey('funds.resources.AccountTypeResource', 'account_type', null=True)
    class Meta:
        queryset = AccountTypeLocale.objects.select_related('account_type').all()
        resource_name = 'accounttypelocale'
        filtering = {
            'locale': ALL,
        }
        authorization = Authorization()

class AccountCategoryResource(ModelResource):
    class Meta:
        queryset = AccountCategory.objects.all()
        resource_name = 'accountcategory'
        authorization = Authorization()

class AccountCategoryLocaleResource(ModelResource):
    account_category_id = fields.ForeignKey('funds.resources.AccountCategoryResource', 'account_category', null=True)
    class Meta:
        queryset = AccountCategoryLocale.objects.select_related('account_category').all()
        resource_name = 'accountcategorylocale'
        filtering = {
            'locale': ALL,
        }
        authorization = Authorization()

class AccountResource(ModelResource):
    client_id = fields.ForeignKey('funds.resources.ClientResource', 'client')
    balance_account_id = fields.ForeignKey('funds.resources.BalanceAccountResource', 'balance_account', null=True)
    saldo_type_id = fields.ForeignKey('funds.resources.AccountSaldoTypeResource', 'saldo_type')
    type_id = fields.ForeignKey('funds.resources.AccountTypeResource', 'type')
    category_id = fields.ForeignKey('funds.resources.AccountCategoryResource', 'category', null=True)
    bank_id = fields.ForeignKey('funds.resources.BankResource', 'bank', null=True)
    parent_client_id = fields.ForeignKey('funds.resources.ClientResource', 'parent_client', null=True)
    user_id = fields.ForeignKey('funds.resources.UserResource', 'user', null=True)
    partitions = fields.ToManyField(PartitionResource, attribute=lambda bundle: AccountPartition.objects.all())
    class Meta:
        limit = 0
        max_limit = 0
        queryset = Account.objects.all()
        resource_name = 'account'
        authorization = Authorization()

class AccountPartitionResource(ModelResource):
    account_id = fields.ForeignKey('funds.resources.AccountResource', 'account')
    partition_id = fields. ForeignKey('funds.resources.PartitionResource', 'partition')
    class Meta:
        queryset = AccountPartition.objects.all()
        resource_name = 'accountpartition'
        filtering = {
            'account_id': ALL,
        }
        authorization = Authorization()

class AccountSaldoTypeResource(ModelResource):
    class Meta:
        limit = 0
        max_limit = 0
        queryset = AccountSaldoType.objects.all()
        resource_name = 'accountsaldotype'
        authorization = Authorization()

class BalanceAccountResource(ModelResource):
    class Meta:
        limit = 0
        max_limit = 0
        queryset = BalanceAccount.objects.all()
        resource_name = 'balanceaccount'
        authorization = Authorization()
