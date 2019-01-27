from django.contrib import auth
from django.db import models

class Users(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return self.username

class Currency(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=5, null=True)
    ISO_digit = models.CharField(max_length=3)
    ISO_char = models.CharField(max_length=3)
    status_id = models.SmallIntegerField()

class AccountClasses(models.Model):
    name = models.CharField(max_length=100)
    inner_name = models.CharField(max_length=100, blank=True, null=True)

class AccountGroups(models.Model):
    name = models.CharField(max_length=200)
    inner_name = models.CharField(max_length=200, blank=True, null=True)

class AccountSaldoTypes(models.Model):
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=3, blank=True, null=True)

class AccountSections(models.Model):
    name = models.CharField(max_length=200)
    inner_name = models.CharField(max_length=200, blank=True, null=True)

class AccountTypes(models.Model):
    name = models.CharField(max_length=30)
    note = models.CharField(max_length=100, blank=True, null=True)

class AccountCategories(models.Model):
    name = models.CharField(max_length=30)
    inner_name = models.CharField(max_length=100, blank=True, null=True)

class Accounts(models.Model):
    number = models.CharField(max_length=300)
    client = models.ForeignKey('Clients', on_delete=models.CASCADE)
    balance_account = models.IntegerField()
    index = models.SmallIntegerField()
    saldo_type = models.ForeignKey('AccountSaldoTypes', on_delete=models.CASCADE)
    type = models.ForeignKey('AccountTypes', on_delete=models.CASCADE)
    category = models.SmallIntegerField(blank=True, null=True)
    bank = models.ForeignKey('Banks', on_delete=models.CASCADE)
    assignment = models.CharField(max_length=300, blank=True, null=True)
    begin_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    parent_client = models.ForeignKey('Clients', related_name='parent_client', on_delete=models.CASCADE)
    sync_partition_flag = models.BooleanField(blank=True, null=True)
    status_id = models.SmallIntegerField()
    user = models.ForeignKey('Users', on_delete=models.PROTECT)
    handle_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('number', 'client', 'balance_account', 'index'),)

class AccountPartitions(models.Model):
    account = models.ForeignKey('Accounts', on_delete=models.CASCADE)
    partition = models.ForeignKey('Partitions', on_delete=models.CASCADE)
    is_primary = models.BooleanField(blank=True, null=True)

    class Meta:
        unique_together = (('account', 'partition'),)

class BalanceAccounts(models.Model):
    balance_number = models.CharField(unique=True, max_length=4)
    assignment = models.CharField(db_column='Assignment', max_length=500, blank=True, null=True)
    inner_assignment = models.CharField(db_column='InnerAssignment', max_length=200, blank=True, null=True)
    saldo_type = models.ForeignKey('AccountSaldoTypes', on_delete=models.CASCADE)
    type = models.ForeignKey('AccountTypes', on_delete=models.CASCADE)

class BankImportPatterns(models.Model):
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

class Banks(models.Model):
    name = models.CharField(max_length=100)
    text_id = models.CharField(unique=True, max_length=300, blank=True, null=True)
    country = models.SmallIntegerField(null=True)
    contact_data = models.CharField(max_length=300, blank=True, null=True)
    user = models.ForeignKey('Users', on_delete=models.PROTECT)
    handle_time = models.DateTimeField(auto_now=True)

class Clients(models.Model):
    name = models.CharField(max_length=500)
    text_id = models.CharField(max_length=300, blank=True, null=True)
    type = models.SmallIntegerField()
    category = models.SmallIntegerField(null=True)
    is_resident = models.BooleanField(default=True)
    responsible_client = models.ForeignKey('self', related_name='clients_responsible_client', on_delete=models.CASCADE, null=True)
    document = models.SmallIntegerField(null=True)
    document_data = models.CharField(max_length=300, blank=True, null=True)
    contact_data = models.CharField(max_length=300, blank=True, null=True)
    add_info = models.CharField(max_length=300, blank=True, null=True)
    attracted_by = models.ForeignKey('self', related_name='attracted_by_client', on_delete=models.CASCADE, null=True)
    status_id = models.BooleanField()
    user = models.ForeignKey('Users', on_delete=models.SET_NULL, blank=True, null=True)
    handle_time = models.DateTimeField(auto_now=True)

class Clientpartitions(models.Model):
    client = models.ForeignKey('Clients', models.CASCADE)
    partition = models.ForeignKey('Partitions', models.CASCADE)
    is_primary = models.BooleanField(null=True)

    class Meta:
        unique_together = (('client', 'partition'),)

class Partitions(models.Model):
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=200, blank=True, null=True)
    client = models.ForeignKey('Clients', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('Users', on_delete=models.PROTECT)
    handle_time = models.DateTimeField(auto_now=True)

class UsersInfo(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE,)
    client = models.ForeignKey('Clients', on_delete=models.SET_NULL, null=True)
    bria_name = models.CharField(max_length=100, null=True)
    status_id = models.SmallIntegerField()

class Bankimport(models.Model):
    linked_transaction_detail = models.ForeignKey('TransactionDetails', on_delete=models.CASCADE, null=True)
    transaction_pattern = models.ForeignKey('TransactionPatterns', on_delete=models.CASCADE)
    import_date = models.DateField()
    file_date = models.DateField()
    file_name = models.CharField(max_length=255)
    bank_import_pattern = models.ForeignKey('BankImportPatterns', on_delete=models.CASCADE)
    is_reverse = models.BooleanField(null=True)
    db_cr_id = models.BooleanField(null=True)
    partition = models.ForeignKey('Partitions', on_delete=models.CASCADE)
    db_bank = models.ForeignKey('Banks', related_name='bankimport_db_bank', on_delete=models.CASCADE, null=True)
    db_bank_text_id = models.CharField(max_length=200, blank=True, null=True)
    db_bank_name = models.CharField(max_length=300, blank=True, null=True)
    db_account = models.ForeignKey('Accounts', related_name='bankimport_db_account', on_delete=models.CASCADE, null=True)
    db_account_number = models.CharField(max_length=300, blank=True, null=True)
    db_client = models.ForeignKey('Clients', related_name='bankimport_db_client', on_delete=models.CASCADE, null=True)
    db_client_text_id = models.CharField(max_length=300, blank=True, null=True)
    db_client_name = models.CharField(max_length=500, blank=True, null=True)
    cr_bank = models.ForeignKey('Banks', related_name='bankimport_cr_bank', on_delete=models.CASCADE, null=True)
    cr_bank_text_id = models.CharField(max_length=200, blank=True, null=True)
    cr_bank_name = models.CharField(max_length=300, blank=True, null=True)
    cr_account = models.ForeignKey('Accounts', related_name='bankimport_cr_account', on_delete=models.CASCADE, null=True)
    cr_account_number = models.CharField(max_length=300, blank=True, null=True)
    cr_client = models.ForeignKey('Clients', related_name='bankimport_cr_client', on_delete=models.CASCADE, null=True)
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
    user = models.ForeignKey('Users', on_delete=models.PROTECT)
    handle_time = models.DateTimeField(auto_now=True)

class TransactionPatterns(models.Model):
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
    user = models.ForeignKey('Users', on_delete=models.PROTECT)
    handle_time = models.DateTimeField(auto_now=True)

class TransactionPatternsFields(models.Model):
    transaction_pattern = models.ForeignKey('TransactionPatterns', on_delete=models.PROTECT)
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

class Transactions(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    pattern = models.ForeignKey('TransactionPatterns', blank=True, null=True, on_delete=models.PROTECT)
    oper_date = models.DateField()
    db_client = models.ForeignKey('Clients', related_name='transactions_db_client', on_delete=models.PROTECT)
    db_account = models.ForeignKey('Accounts', related_name='transactions_db_account', on_delete=models.PROTECT, blank=True, null=True)
    cr_client = models.ForeignKey('Clients', related_name='transactions_cr_client', on_delete=models.PROTECT)
    cr_account = models.ForeignKey('Accounts', related_name='transactions_cr_account', on_delete=models.PROTECT, blank=True, null=True)
    currency_rate = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    exchange_income = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    partition = models.ForeignKey('Partitions', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    amount_e = models.DecimalField(max_digits=15, decimal_places=2)
    exchange_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    exchange_amount_e = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    currency = models.ForeignKey('Currency', related_name='transactions_currency', on_delete=models.PROTECT)
    exchange_currency = models.ForeignKey('Currency', related_name='transactions_exchange_currency', on_delete=models.PROTECT, blank=True, null=True)
    payment_details = models.CharField(max_length=1000, blank=True, null=True)
    addinfo = models.CharField(max_length=200, blank=True, null=True)
    bankimport = models.ForeignKey('Bankimport', on_delete=models.SET_NULL, blank=True, null=True)
    status_id = models.SmallIntegerField()
    user = models.ForeignKey('Users', on_delete=models.PROTECT, blank=True, null=True)
    handle_time = models.DateTimeField(auto_now=True)

class TransactionDetails(models.Model):
    # transaction = models.ForeignKey('Transactions', on_delete=models.CASCADE)
    transaction = models.IntegerField()
    order_id = models.SmallIntegerField()
    partition = models.ForeignKey('Partitions', on_delete=models.PROTECT)
    db_client = models.ForeignKey('Clients', related_name='db_client', on_delete=models.PROTECT)
    db_account = models.ForeignKey('Accounts', related_name='db_account', on_delete=models.PROTECT)
    cr_client = models.ForeignKey('Clients', related_name='cr_client', on_delete=models.PROTECT)
    cr_account = models.ForeignKey('Accounts', related_name='cr_account', on_delete=models.PROTECT)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    amount_e = models.DecimalField(max_digits=15, decimal_places=2)
    status_id = models.SmallIntegerField()
    user = models.ForeignKey('Users', on_delete=models.PROTECT)
    handle_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('transaction', 'order_id'),)

class TransactionPatternsScheme(models.Model):
    pattern = models.ForeignKey('TransactionPatterns', on_delete=models.PROTECT)
    order_id = models.SmallIntegerField(null=True)
    db_account_field = models.ForeignKey('TransactionPatternsFields', related_name='transactions_patterns_scheme_db_account_field', on_delete=models.PROTECT, null=True)
    db_balance_account = models.ForeignKey('BalanceAccounts', related_name='transactions_patterns_scheme_db_balance_account', on_delete=models.PROTECT, null=True)
    db_account_index = models.SmallIntegerField(null=True)
    db_account_type = models.ForeignKey('AccountTypes', related_name='transactions_patterns_scheme_db_account_type', on_delete=models.PROTECT, null=True)
    db_account_category = models.ForeignKey('AccountCategories', related_name='transactions_patterns_scheme_db_account_category', on_delete=models.PROTECT, null=True)
    db_client_field = models.ForeignKey('TransactionPatternsFields', related_name='transactions_patterns_scheme_db_client_field', on_delete=models.PROTECT, null=True)
    db_client = models.ForeignKey('Clients', related_name='transactions_patterns_scheme_db_client', on_delete=models.PROTECT)
    cr_account_field = models.ForeignKey('TransactionPatternsFields', related_name='transactions_patterns_scheme_cr_account_field', on_delete=models.PROTECT, null=True)
    cr_balance_account = models.ForeignKey('BalanceAccounts', related_name='transactions_patterns_scheme_cr_balance_account', on_delete=models.PROTECT, null=True)
    cr_account_index = models.SmallIntegerField(null=True)
    cr_account_type = models.ForeignKey('AccountTypes', related_name='transactions_patterns_scheme_cr_account_type', on_delete=models.PROTECT, null=True)
    cr_account_category = models.ForeignKey('AccountCategories', related_name='transactions_patterns_scheme_cr_account_category', on_delete=models.PROTECT, null=True)
    cr_client_field = models.ForeignKey('TransactionPatternsFields', related_name='transactions_patterns_scheme_cr_client_field', on_delete=models.PROTECT, null=True)
    cr_client = models.ForeignKey('Clients', related_name='transactions_patterns_scheme_cr_client', on_delete=models.PROTECT)
    amount_sql = models.CharField(max_length=1000)
    currency_field = models.ForeignKey('TransactionPatternsFields', on_delete=models.PROTECT, null=True)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT, null=True)
    partition = models.ForeignKey('Partitions', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey('Users', on_delete=models.PROTECT)
    handle_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('pattern', 'order_id'),)

class TransactionTaxes(models.Model):
    transaction = models.ForeignKey('Transactions', on_delete=models.PROTECT)
    order_id = models.SmallIntegerField()
    db_client = models.ForeignKey('Clients', related_name='transaction_taxes_db_client', on_delete=models.PROTECT, null=True)
    cr_client = models.ForeignKey('Clients', related_name='transaction_taxes_cr_client', on_delete=models.PROTECT, null=True)
    rate = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    rate_method = models.SmallIntegerField(null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    amount_e = models.DecimalField(max_digits=15, decimal_places=2)
    status_id = models.SmallIntegerField(null=True)
    user = models.ForeignKey('Users', on_delete=models.PROTECT)
    handle_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('transaction', 'order_id'),)

class UserPartitions(models.Model):
    user = models.ForeignKey('Users', models.CASCADE)
    partition = models.ForeignKey('Partitions', models.CASCADE)
    is_primary = models.BooleanField(null=True)

    class Meta:
        unique_together = (('user', 'partition'),)
