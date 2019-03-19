from django.contrib import auth
from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

class Partition(models.Model):
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=200, blank=True, null=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
    handle_time = models.DateTimeField(auto_now=True)

class ClientType(models.Model):
    name = models.CharField(max_length=30)
    note = models.CharField(max_length=100, blank=True, null=True)


class ClientTypeLocale(models.Model):
    locale = models.CharField(max_length=2)
    client_type = models.ForeignKey('ClientType', on_delete=models.CASCADE)
    # client_type = models.IntegerField()
    name = models.CharField(max_length=30)
    note = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('locale', 'client_type'),)

class ClientCategory(models.Model):
    name = models.CharField(max_length=30)
    note = models.CharField(max_length=100, blank=True, null=True)

class ClientCategoryLocale(models.Model):
    locale = models.CharField(max_length=2)
    client_category = models.ForeignKey('ClientCategory', on_delete=models.CASCADE)
    # client_type = models.IntegerField()
    name = models.CharField(max_length=30)
    note = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('locale', 'client_category'),)

class Client(models.Model):
    name = models.CharField(max_length=500)
    # latin_name = models.CharField(max_length=500)
    text_id = models.CharField(max_length=300, blank=True, null=True)
    type = models.ForeignKey('ClientType', on_delete=models.SET_NULL, default=3, blank=True, null=True)
    category = models.ForeignKey('ClientCategory', on_delete=models.PROTECT, blank=True, null=True)
    # type = models.SmallIntegerField(blank=True, null=True)
    # category = models.SmallIntegerField(blank=True, null=True)
    is_resident = models.BooleanField(default=True)
    responsible_client = models.ForeignKey('self', related_name='client_responsible_client', on_delete=models.SET_NULL, blank=True, null=True)
    document = models.SmallIntegerField(blank=True, null=True)
    document_data = models.CharField(max_length=300, blank=True, null=True)
    contact_data = models.CharField(max_length=300, blank=True, null=True)
    add_info = models.CharField(max_length=300, blank=True, null=True)
    attracted_by = models.ForeignKey('self', related_name='attracted_by_client', on_delete=models.SET_NULL, blank=True, null=True)
    status_id = models.SmallIntegerField(default='1')
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
    handle_time = models.DateTimeField(auto_now=True)

class ClientPartition(models.Model):
    client = models.ForeignKey('Client', models.CASCADE)
    partition = models.ForeignKey('Partition', models.CASCADE)
    is_primary = models.BooleanField(null=True)

    class Meta:
        unique_together = (('client', 'partition'),)

class Country(models.Model):
    name = models.CharField(max_length=100)
    latin_name = models.CharField(max_length=100, blank=True, null=True)
    ISO_digit = models.CharField(max_length=3)
    ISO_char = models.CharField(max_length=3)
    ISO_short_char = models.CharField(max_length=2)

class Currency(models.Model):
    name = models.CharField(max_length=100)
    latin_name = models.CharField(max_length=100, blank=True, null=True)
    ISO_digit = models.CharField(max_length=3)
    ISO_char = models.CharField(max_length=3)
    status_id = models.SmallIntegerField(default=1)

class AccountClass(models.Model):
    name = models.CharField(max_length=100)
    inner_name = models.CharField(max_length=100, blank=True, null=True)

class AccountGroup(models.Model):
    name = models.CharField(max_length=200)
    inner_name = models.CharField(max_length=200, blank=True, null=True)

class AccountSaldoType(models.Model):
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=3, blank=True, null=True)

class AccountSection(models.Model):
    name = models.CharField(max_length=200)
    inner_name = models.CharField(max_length=200, blank=True, null=True)

class AccountType(models.Model):
    name = models.CharField(max_length=30)
    note = models.CharField(max_length=100, blank=True, null=True)

class AccountTypeLocale(models.Model):
    locale = models.CharField(max_length=2)
    account_type = models.ForeignKey('AccountType', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    note = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        unique_together = (('locale', 'account_type'),)

class AccountCategory(models.Model):
    name = models.CharField(max_length=30)
    inner_name = models.CharField(max_length=100, blank=True, null=True)

class AccountCategoryLocale(models.Model):
    locale = models.CharField(max_length=2)
    account_category = models.ForeignKey('AccountCategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    inner_name = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        unique_together = (('locale', 'account_category'),)

class Account(models.Model):
    number = models.CharField(max_length=300)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    balance_account = models.ForeignKey('BalanceAccount', on_delete=models.PROTECT)
    index = models.SmallIntegerField()
    saldo_type = models.ForeignKey('AccountSaldoType', on_delete=models.PROTECT)
    type = models.ForeignKey('AccountType', on_delete=models.PROTECT)
    category = models.ForeignKey('AccountCategory', on_delete=models.SET_NULL, blank=True, null=True)
    bank = models.ForeignKey('Bank', on_delete=models.SET_NULL, blank=True, null=True)
    assignment = models.CharField(max_length=300, blank=True, null=True)
    begin_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    parent_client = models.ForeignKey('Client', related_name='parent_client', on_delete=models.SET_NULL, blank=True, null=True)
    sync_partition_flag = models.BooleanField(blank=True, null=True, default=True)
    status_id = models.SmallIntegerField(default=1)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
    handle_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('number', 'client', 'balance_account', 'index'),)

class AccountPartition(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    partition = models.ForeignKey('Partition', on_delete=models.CASCADE)
    is_primary = models.BooleanField(blank=True, null=True)

    class Meta:
        unique_together = (('account', 'partition'),)

class AccountPartitionCart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    partition = models.ForeignKey('Partition', on_delete=models.CASCADE)
    is_primary = models.BooleanField(blank=True, null=True)

    class Meta:
        unique_together = (('user', 'account', 'partition'),)

class BalanceAccount(models.Model):
    balance_number = models.CharField(unique=True, max_length=4)
    assignment = models.CharField(max_length=500, blank=True, null=True)
    inner_assignment = models.CharField(max_length=200, blank=True, null=True)
    saldo_type = models.ForeignKey('AccountSaldoType', on_delete=models.CASCADE)
    type = models.ForeignKey('AccountType', on_delete=models.CASCADE)

class BankImportPattern(models.Model):
    name = models.CharField(max_length=100)
    file_format_id = models.SmallIntegerField()
    map = models.CharField(max_length=1000)
    skip_first_rows = models.IntegerField(null=True)
    skip_first_cols = models.IntegerField(null=True)
    delimiter = models.CharField(max_length=1, blank=True, null=True)
    quote = models.CharField(max_length=1, blank=True, null=True)
    file_extentions = models.CharField(max_length=100)
    after_sql = models.CharField(max_length=1000, blank=True, null=True)
    is_resident = models.BooleanField()
    is_active = models.BooleanField()
    encoding_id = models.SmallIntegerField(null=True)

class Bank(models.Model):
    name = models.CharField(max_length=100)
    text_id = models.CharField(unique=True, max_length=300, blank=True, null=True)
    country = models.ForeignKey('Country', null=True, blank=True, on_delete=models.SET_NULL)
    contact_data = models.CharField(max_length=300, blank=True, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
    handle_time = models.DateTimeField(auto_now=True)

class Bankimport(models.Model):
    linked_transaction_detail = models.ForeignKey('TransactionDetail', on_delete=models.CASCADE, null=True)
    transaction_pattern = models.ForeignKey('TransactionPattern', on_delete=models.CASCADE)
    import_date = models.DateField()
    file_date = models.DateField()
    file_name = models.CharField(max_length=255)
    bank_import_pattern = models.ForeignKey('BankImportPattern', on_delete=models.CASCADE)
    is_reverse = models.BooleanField(null=True)
    db_cr_id = models.BooleanField(null=True)
    partition = models.ForeignKey('Partition', on_delete=models.CASCADE)
    db_bank = models.ForeignKey('Bank', related_name='bankimport_db_bank', on_delete=models.CASCADE, null=True)
    db_bank_text_id = models.CharField(max_length=200, blank=True, null=True)
    db_bank_name = models.CharField(max_length=300, blank=True, null=True)
    db_account = models.ForeignKey('Account', related_name='bankimport_db_account', on_delete=models.CASCADE, null=True)
    db_account_number = models.CharField(max_length=300, blank=True, null=True)
    db_client = models.ForeignKey('Client', related_name='bankimport_db_client', on_delete=models.CASCADE, null=True)
    db_client_text_id = models.CharField(max_length=300, blank=True, null=True)
    db_client_name = models.CharField(max_length=500, blank=True, null=True)
    cr_bank = models.ForeignKey('Bank', related_name='bankimport_cr_bank', on_delete=models.CASCADE, null=True)
    cr_bank_text_id = models.CharField(max_length=200, blank=True, null=True)
    cr_bank_name = models.CharField(max_length=300, blank=True, null=True)
    cr_account = models.ForeignKey('Account', related_name='bankimport_cr_account', on_delete=models.CASCADE, null=True)
    cr_account_number = models.CharField(max_length=300, blank=True, null=True)
    cr_client = models.ForeignKey('Client', related_name='bankimport_cr_client', on_delete=models.CASCADE, null=True)
    cr_client_text_id = models.CharField(max_length=300, blank=True, null=True)
    cr_client_name = models.CharField(max_length=500, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    add_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT, null=True)
    currency_text_id = models.CharField(max_length=100, blank=True, null=True)
    tax_date = models.DateField(blank=True, null=True)
    payment_details = models.CharField(max_length=1000, blank=True, null=True)
    add_info = models.CharField(max_length=200, blank=True, null=True)
    status_id = models.SmallIntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
    handle_time = models.DateTimeField(auto_now=True)

class TransactionPattern(models.Model):
    name = models.CharField(max_length=100)
    type = models.SmallIntegerField()
    category = models.SmallIntegerField()
    parent_id = models.ForeignKey('self', on_delete=models.DO_NOTHING)
    order_id = models.IntegerField()
    icon_id = models.IntegerField(null=True)
    level_id = models.SmallIntegerField()
    form_width = models.IntegerField(null=True)
    form_height = models.IntegerField(null=True)
    after_sql = models.CharField(max_length=1000, blank=True, null=True)
    status_id = models.SmallIntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
    handle_time = models.DateTimeField(auto_now=True)

class TransactionPatternField(models.Model):
    transaction_pattern = models.ForeignKey('TransactionPattern', on_delete=models.PROTECT)
    field_type_id = models.BooleanField()
    tax_order_id = models.SmallIntegerField(null=True)
    field_name = models.CharField(max_length=100)
    caption = models.CharField(max_length=100, blank=True, null=True)
    is_read_only = models.BooleanField(null=True)
    control_id = models.SmallIntegerField()
    width = models.SmallIntegerField()
    defaultvalue = models.CharField(max_length=1000, blank=True, null=True)
    is_required = models.BooleanField(null=True)
    font_style = models.SmallIntegerField(null=True)
    font_color = models.CharField(max_length=50, null=True)
    dictionary_sql = models.CharField(max_length=1000, blank=True, null=True)
    format = models.CharField(max_length=50, blank=True, null=True)
    left = models.SmallIntegerField()

class Transaction(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    pattern = models.ForeignKey('TransactionPattern', blank=True, null=True, on_delete=models.PROTECT)
    oper_date = models.DateField(auto_now=True)
    db_client = models.ForeignKey('Client', related_name='transaction_db_client', on_delete=models.PROTECT, verbose_name='-Дт Клиент-')
    db_account = models.ForeignKey('Account', related_name='transaction_db_account', on_delete=models.PROTECT, blank=True, null=True)
    cr_client = models.ForeignKey('Client', related_name='transaction_cr_client', on_delete=models.PROTECT)
    cr_account = models.ForeignKey('Account', related_name='transaction_cr_account', on_delete=models.PROTECT, blank=True, null=True)
    currency_rate = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    exchange_income = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    partition = models.ForeignKey('Partition', on_delete=models.PROTECT, default=1)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    amount_e = models.DecimalField(max_digits=15, decimal_places=2)
    exchange_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    exchange_amount_e = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    currency = models.ForeignKey('Currency', related_name='transaction_currency', on_delete=models.PROTECT)
    exchange_currency = models.ForeignKey('Currency', related_name='transaction_exchange_currency', on_delete=models.PROTECT, blank=True, null=True)
    payment_details = models.CharField(max_length=1000, blank=True, null=True)
    addinfo = models.CharField(max_length=200, blank=True, null=True)
    bankimport = models.ForeignKey('Bankimport', on_delete=models.SET_NULL, blank=True, null=True)
    status_id = models.SmallIntegerField(choices=(('1', 'проведена'), ('2', 'отложена'), ('3', 'сторно')), default=1)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True, default=User)
    handle_time = models.DateTimeField(auto_now=True)

class TransactionDetail(models.Model):
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    # transaction = models.IntegerField()
    order_id = models.SmallIntegerField()
    partition = models.ForeignKey('Partition', on_delete=models.PROTECT)
    db_client = models.ForeignKey('Client', related_name='db_client', on_delete=models.PROTECT)
    db_account = models.ForeignKey('Account', related_name='db_account', on_delete=models.PROTECT)
    cr_client = models.ForeignKey('Client', related_name='cr_client', on_delete=models.PROTECT)
    cr_account = models.ForeignKey('Account', related_name='cr_account', on_delete=models.PROTECT)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    amount_e = models.DecimalField(max_digits=15, decimal_places=2)
    status_id = models.SmallIntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
    handle_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('transaction', 'order_id'),)

class TransactionPatternScheme(models.Model):
    pattern = models.ForeignKey('TransactionPattern', on_delete=models.PROTECT)
    order_id = models.SmallIntegerField(null=True)
    db_account_field = models.ForeignKey('TransactionPatternField', related_name='transaction_pattern_scheme_db_account_field', on_delete=models.PROTECT, null=True)
    db_balance_account = models.ForeignKey('BalanceAccount', related_name='transaction_pattern_scheme_db_balance_account', on_delete=models.PROTECT, null=True)
    db_account_index = models.SmallIntegerField(null=True)
    db_account_type = models.ForeignKey('AccountType', related_name='transaction_pattern_scheme_db_account_type', on_delete=models.PROTECT, null=True)
    db_account_category = models.ForeignKey('AccountCategory', related_name='transaction_pattern_scheme_db_account_category', on_delete=models.PROTECT, null=True)
    db_client_field = models.ForeignKey('TransactionPatternField', related_name='transaction_pattern_scheme_db_client_field', on_delete=models.PROTECT, null=True)
    db_client = models.ForeignKey('Client', related_name='transaction_pattern_scheme_db_client', on_delete=models.PROTECT)
    cr_account_field = models.ForeignKey('TransactionPatternField', related_name='transaction_pattern_scheme_cr_account_field', on_delete=models.PROTECT, null=True)
    cr_balance_account = models.ForeignKey('BalanceAccount', related_name='transaction_pattern_scheme_cr_balance_account', on_delete=models.PROTECT, null=True)
    cr_account_index = models.SmallIntegerField(null=True)
    cr_account_type = models.ForeignKey('AccountType', related_name='transaction_pattern_scheme_cr_account_type', on_delete=models.PROTECT, null=True)
    cr_account_category = models.ForeignKey('AccountCategory', related_name='transaction_pattern_scheme_cr_account_category', on_delete=models.PROTECT, null=True)
    cr_client_field = models.ForeignKey('TransactionPatternField', related_name='transaction_pattern_scheme_cr_client_field', on_delete=models.PROTECT, null=True)
    cr_client = models.ForeignKey('Client', related_name='transaction_pattern_scheme_cr_client', on_delete=models.PROTECT)
    amount_sql = models.CharField(max_length=1000)
    currency_field = models.ForeignKey('TransactionPatternField', on_delete=models.PROTECT, null=True)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT, null=True)
    partition = models.ForeignKey('Partition', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
    handle_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('pattern', 'order_id'),)

class TransactionTax(models.Model):
    transaction = models.ForeignKey('Transaction', on_delete=models.PROTECT)
    order_id = models.SmallIntegerField()
    db_client = models.ForeignKey('Client', related_name='transaction_tax_db_client', on_delete=models.PROTECT, null=True)
    cr_client = models.ForeignKey('Client', related_name='transaction_tax_cr_client', on_delete=models.PROTECT, null=True)
    rate = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    rate_method = models.SmallIntegerField(null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    amount_e = models.DecimalField(max_digits=15, decimal_places=2)
    status_id = models.SmallIntegerField(null=True)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
    handle_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('transaction', 'order_id'),)

class UserPartitions(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    partition = models.ForeignKey('Partition', models.CASCADE)
    is_primary = models.BooleanField(null=True)

    class Meta:
        unique_together = (('user', 'partition'),)
