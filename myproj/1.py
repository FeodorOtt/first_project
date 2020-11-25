# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountClasses(models.Model):
    name = models.CharField(max_length=100)
    inner_name = models.CharField(max_length=100, blank=True, null=True)


class AccountGroups(models.Model):
    name = models.CharField(max_length=200)
    inner_name = models.CharField(ax_length=200, blank=True, null=True)


class AccountPartitions(models.Model):
    account = models.ForeignKey('Accounts', on_delete=models.CASCADE)
    partition = models.ForeignKey('Partitions', on_delete=models.CASCADE)
    is_primary = models.TextField(db_column='IsPrimary', blank=True, null=True) This field type is a guess.

    class Meta:
        managed = False
        db_table = 'AccountPartitions'
        unique_together = (('accountid', 'partitionid'),)


class Accountsaldotype(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=30)
    shortname = models.CharField(db_column='ShortName', max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AccountSaldoType'


class Accountsections(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=200)
    innername = models.CharField(db_column='InnerName', max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AccountSections'


class Accounttype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=30)
    note = models.CharField(db_column='Note', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AccountType'


class Accounts(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    number = models.CharField(db_column='Number', max_length=300)
    clientid = models.IntegerField(db_column='ClientID')
    balanceaccountid = models.IntegerField(db_column='BalanceAccountID')
    index = models.SmallIntegerField(db_column='Index')
    saldotypeid = models.SmallIntegerField(db_column='SaldoTypeID')
    typeid = models.SmallIntegerField(db_column='TypeID')
    categoryid = models.SmallIntegerField(db_column='CategoryID', blank=True, null=True)
    bankid = models.IntegerField(db_column='BankID', blank=True, null=True)
    assignment = models.CharField(db_column='Assignment', max_length=300, blank=True, null=True)
    begindate = models.DateField(db_column='BeginDate')
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)
    parentclientid = models.IntegerField(db_column='ParentClientID', blank=True, null=True)
    syncpartitionflag = models.TextField(db_column='SyncPartitionFlag', blank=True, null=True) This field type is a guess.
    statusid = models.SmallIntegerField(db_column='StatusID')
    userid = models.IntegerField(db_column='UserID')
    handletime = models.DateTimeField(db_column='HandleTime')

    class Meta:
        managed = False
        db_table = 'Accounts'
        unique_together = (('number', 'clientid', 'balanceaccountid', 'index'),)


class Balanceaccounts(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    balancenumber = models.CharField(db_column='BalanceNumber', unique=True, max_length=4)
    assignment = models.CharField(db_column='Assignment', max_length=200, blank=True, null=True)
    innerassignment = models.CharField(db_column='InnerAssignment', max_length=200, blank=True, null=True)
    saldotypeid = models.SmallIntegerField(db_column='SaldoTypeID')
    typeid = models.SmallIntegerField(db_column='TypeID')

    class Meta:
        managed = False
        db_table = 'BalanceAccounts'


class Bankimport(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    linkedid = models.IntegerField(db_column='LinkedID', blank=True, null=True)
    transactionpatternid = models.IntegerField(db_column='TransactionPatternID')
    importdate = models.DateField(db_column='ImportDate')
    filedate = models.DateField(db_column='FileDate')
    filename = models.CharField(db_column='FileName', max_length=255)
    bankimportpatternid = models.IntegerField(db_column='BankImportPatternID')
    isreverse = models.TextField(db_column='IsReverse', blank=True, null=True) This field type is a guess.
    dbcrid = models.TextField(db_column='DbCrID', blank=True, null=True) This field type is a guess.
    partitionid = models.IntegerField(db_column='PartitionID')
    dbbankid = models.IntegerField(db_column='DbBankID', blank=True, null=True)
    dbbanktextid = models.CharField(db_column='DbBankTextID', max_length=200, blank=True, null=True)
    dbbankname = models.CharField(db_column='DbBankName', max_length=300, blank=True, null=True)
    dbaccountid = models.IntegerField(db_column='DbAccountID', blank=True, null=True)
    dbaccountnumber = models.CharField(db_column='DbAccountNumber', max_length=300, blank=True, null=True)
    dbclientid = models.IntegerField(db_column='DbClientID', blank=True, null=True)
    dbclienttextid = models.CharField(db_column='DbClientTextID', max_length=300, blank=True, null=True)
    dbclientname = models.CharField(db_column='DbClientName', max_length=500, blank=True, null=True)
    crbankid = models.IntegerField(db_column='CrBankID', blank=True, null=True)
    crbanktextid = models.CharField(db_column='CrBankTextID', max_length=200, blank=True, null=True)
    crbankname = models.CharField(db_column='CrBankName', max_length=300, blank=True, null=True)
    craccountid = models.IntegerField(db_column='CrAccountID', blank=True, null=True)
    craccountnumber = models.CharField(db_column='CrAccountNumber', max_length=300, blank=True, null=True)
    crclientid = models.IntegerField(db_column='CrClientID', blank=True, null=True)
    crclienttextid = models.CharField(db_column='CrClientTextID', max_length=300, blank=True, null=True)
    crclientname = models.CharField(db_column='CrClientName', max_length=500, blank=True, null=True)
    amount = models.DecimalField(db_column='Amount', max_digits=15, decimal_places=2)
    addamount = models.DecimalField(db_column='AddAmount', max_digits=15, decimal_places=2, blank=True, null=True)
    currencyid = models.IntegerField(db_column='CurrencyID', blank=True, null=True)
    currencytextid = models.CharField(db_column='CurrencyTextID', max_length=100, blank=True, null=True)
    taxdate = models.DateField(db_column='TaxDate', blank=True, null=True)
    paymentdetails = models.CharField(db_column='PaymentDetails', max_length=-1, blank=True, null=True)
    addinfo = models.CharField(db_column='AddInfo', max_length=200, blank=True, null=True)
    statusid = models.SmallIntegerField(db_column='StatusID')
    userid = models.IntegerField(db_column='UserID')
    handletime = models.DateTimeField(db_column='HandleTime')

    class Meta:
        managed = False
        db_table = 'BankImport'


class Bankimportpatterns(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    fileformatid = models.SmallIntegerField(db_column='FileFormatID')
    map = models.CharField(db_column='Map', max_length=-1)
    skipfirstrows = models.IntegerField(db_column='SkipFirstRows', blank=True, null=True)
    skipfirstcols = models.IntegerField(db_column='SkipFirstCols', blank=True, null=True)
    delimiter = models.CharField(db_column='Delimiter', max_length=1, blank=True, null=True)
    quote = models.CharField(db_column='Quote', max_length=1, blank=True, null=True)
    fileextentions = models.CharField(db_column='FileExtentions', max_length=100)
    aftersql = models.CharField(db_column='AfterSQL', max_length=-1, blank=True, null=True)
    isresident = models.TextField(db_column='IsResident') This field type is a guess.
    isactive = models.TextField(db_column='IsActive') This field type is a guess.
    encodingid = models.SmallIntegerField(db_column='EncodingID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BankImportPatterns'


class Banks(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    textid = models.CharField(db_column='TextID', unique=True, max_length=300, blank=True, null=True)
    countryid = models.SmallIntegerField(db_column='CountryID', blank=True, null=True)
    contactdata = models.CharField(db_column='ContactData', max_length=300, blank=True, null=True)
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)
    handletime = models.DateTimeField(db_column='HandleTime', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Banks'


class Clientpartitions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    clientid = models.ForeignKey('Clients', models.DO_NOTHING, db_column='ClientID')
    partitionid = models.ForeignKey('Partitions', models.DO_NOTHING, db_column='PartitionID')
    isprimary = models.TextField(db_column='IsPrimary', blank=True, null=True) This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ClientPartitions'
        unique_together = (('clientid', 'partitionid'),)


class Clients(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=500)
    textid = models.CharField(db_column='TextID', max_length=300, blank=True, null=True)
    typeid = models.SmallIntegerField(db_column='TypeID')
    categoryid = models.SmallIntegerField(db_column='CategoryID', blank=True, null=True)
    residentid = models.TextField(db_column='ResidentID', blank=True, null=True) This field type is a guess.
    responsibleclientid = models.IntegerField(db_column='ResponsibleClientID', blank=True, null=True)
    documentid = models.SmallIntegerField(db_column='DocumentID', blank=True, null=True)
    documentdata = models.CharField(db_column='DocumentData', max_length=300, blank=True, null=True)
    contactdata = models.CharField(db_column='ContactData', max_length=300, blank=True, null=True)
    addinfo = models.CharField(db_column='AddInfo', max_length=300, blank=True, null=True)
    attractedby = models.ForeignKey('self', models.DO_NOTHING, db_column='AttractedBy', blank=True, null=True)
    statusid = models.TextField(db_column='StatusID') This field type is a guess.
    userid = models.IntegerField(db_column='UserID')
    handletime = models.DateTimeField(db_column='HandleTime')

    class Meta:
        managed = False
        db_table = 'Clients'


class Partitions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    note = models.CharField(db_column='Note', max_length=200, blank=True, null=True)
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)
    userid = models.IntegerField(db_column='UserID')
    handletime = models.DateTimeField(db_column='HandleTime')

    class Meta:
        managed = False
        db_table = 'Partitions'


class Transactiondetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    transactionid = models.IntegerField(db_column='TransactionID')
    orderid = models.SmallIntegerField(db_column='OrderID')
    partitionid = models.IntegerField(db_column='PartitionID')
    dbclientid = models.IntegerField(db_column='DbClientID')
    dbaccountid = models.IntegerField(db_column='DbAccountID')
    crclientid = models.IntegerField(db_column='CrClientID')
    craccountid = models.IntegerField(db_column='CrAccountID')
    currencyid = models.IntegerField(db_column='CurrencyID')
    amount = models.DecimalField(db_column='Amount', max_digits=15, decimal_places=2)
    amount_e = models.DecimalField(db_column='Amount_E', max_digits=15, decimal_places=2)
    statusid = models.SmallIntegerField(db_column='StatusID')
    userid = models.IntegerField(db_column='UserID')
    handletime = models.DateTimeField(db_column='HandleTime')

    class Meta:
        managed = False
        db_table = 'TransactionDetails'
        unique_together = (('transactionid', 'orderid'),)


class Transactionpatternsfields(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    transactionpatternid = models.IntegerField(db_column='TransactionPatternID')
    fieldtypeid = models.TextField(db_column='FieldTypeID') This field type is a guess.
    taxorderid = models.SmallIntegerField(db_column='TaxOrderID', blank=True, null=True)
    fieldname = models.CharField(db_column='FieldName', max_length=100)
    caption = models.CharField(db_column='Caption', max_length=100, blank=True, null=True)
    isreadonly = models.TextField(db_column='IsReadOnly', blank=True, null=True) This field type is a guess.
    controlid = models.SmallIntegerField(db_column='ControlID')
    width = models.SmallIntegerField(db_column='Width')
    defaultvalue = models.CharField(db_column='DefaultValue', max_length=-1, blank=True, null=True)
    isrequired = models.TextField(db_column='IsRequired', blank=True, null=True) This field type is a guess.
    fontstyle = models.SmallIntegerField(db_column='FontStyle', blank=True, null=True)
    fontcolor = models.SmallIntegerField(db_column='FontColor', blank=True, null=True)
    dictionarysql = models.CharField(db_column='DictionarySQL', max_length=-1, blank=True, null=True)
    format = models.CharField(db_column='Format', max_length=50, blank=True, null=True)
    left = models.SmallIntegerField(db_column='Left')

    class Meta:
        managed = False
        db_table = 'TransactionPatternsFields'


class Transactionpatternsscheme(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    patternid = models.IntegerField(db_column='PatternID')
    orderid = models.SmallIntegerField(db_column='OrderID')
    dbaccountfieldid = models.SmallIntegerField(db_column='DbAccountFieldID', blank=True, null=True)
    dbbalanceaccountid = models.IntegerField(db_column='DbBalanceAccountID', blank=True, null=True)
    dbaccountindex = models.SmallIntegerField(db_column='DbAccountIndex', blank=True, null=True)
    dbaccounttypeid = models.SmallIntegerField(db_column='DbAccountTypeID', blank=True, null=True)
    dbaccountcategoryid = models.SmallIntegerField(db_column='DbAccountCategoryID', blank=True, null=True)
    dbclientfieldid = models.SmallIntegerField(db_column='DbClientFieldID', blank=True, null=True)
    dbclientid = models.IntegerField(db_column='DbClientID', blank=True, null=True)
    craccountfieldid = models.SmallIntegerField(db_column='CrAccountFieldID', blank=True, null=True)
    crbalanceaccountid = models.IntegerField(db_column='CrBalanceAccountID', blank=True, null=True)
    craccountindex = models.SmallIntegerField(db_column='CrAccountIndex', blank=True, null=True)
    craccounttypeid = models.SmallIntegerField(db_column='CrAccountTypeID', blank=True, null=True)
    craccountcategoryid = models.SmallIntegerField(db_column='CrAccountCategoryID', blank=True, null=True)
    crclientfieldid = models.SmallIntegerField(db_column='CrClientFieldID', blank=True, null=True)
    crclientid = models.IntegerField(db_column='CrClientID', blank=True, null=True)
    amountsql = models.CharField(db_column='AmountSQL', max_length=-1)
    currencyfieldid = models.SmallIntegerField(db_column='CurrencyFieldID', blank=True, null=True)
    currencyid = models.IntegerField(db_column='CurrencyID', blank=True, null=True)
    partitionid = models.IntegerField(db_column='PartitionID', blank=True, null=True)
    userid = models.IntegerField(db_column='UserID')
    handletime = models.DateTimeField(db_column='HandleTime')

    class Meta:
        managed = False
        db_table = 'TransactionPatternsScheme'
        unique_together = (('patternid', 'orderid'),)


class Transactiontaxes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    transactionid = models.IntegerField(db_column='TransactionID')
    orderid = models.SmallIntegerField(db_column='OrderID')
    dbclientid = models.IntegerField(db_column='DbClientID', blank=True, null=True)
    crclientid = models.IntegerField(db_column='CrClientID', blank=True, null=True)
    rate = models.DecimalField(db_column='Rate', max_digits=15, decimal_places=6, blank=True, null=True)
    ratemethodid = models.SmallIntegerField(db_column='RateMethodID', blank=True, null=True)
    amount = models.DecimalField(db_column='Amount', max_digits=15, decimal_places=2)
    amount_e = models.DecimalField(db_column='Amount_E', max_digits=15, decimal_places=2)
    statusid = models.SmallIntegerField(db_column='StatusID', blank=True, null=True)
    userid = models.IntegerField(db_column='UserID')
    handletime = models.DateTimeField(db_column='HandleTime')

    class Meta:
        managed = False
        db_table = 'TransactionTaxes'
        unique_together = (('transactionid', 'orderid'),)


class Transactions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)
    patternid = models.IntegerField(db_column='PatternID')
    operdate = models.DateField(db_column='OperDate')
    dbclientid = models.IntegerField(db_column='DbClientID')
    dbaccountid = models.IntegerField(db_column='DbAccountID', blank=True, null=True)
    crclientid = models.IntegerField(db_column='CrClientID')
    craccountid = models.IntegerField(db_column='CrAccountID', blank=True, null=True)
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=15, decimal_places=10, blank=True, null=True)
    exchangeincome = models.DecimalField(db_column='ExchangeIncome', max_digits=15, decimal_places=2, blank=True, null=True)
    partitionid = models.IntegerField(db_column='PartitionID')
    amount = models.DecimalField(db_column='Amount', max_digits=15, decimal_places=2)
    amount_e = models.DecimalField(db_column='Amount_E', max_digits=15, decimal_places=2)
    exchangeamount = models.DecimalField(db_column='ExchangeAmount', max_digits=15, decimal_places=2, blank=True, null=True)
    exchangeamount_e = models.DecimalField(db_column='ExchangeAmount_E', max_digits=15, decimal_places=2, blank=True, null=True)
    currencyid = models.IntegerField(db_column='CurrencyID')
    exchangecurrencyid = models.IntegerField(db_column='ExchangeCurrencyID', blank=True, null=True)
    paymentdetails = models.CharField(db_column='PaymentDetails', max_length=-1, blank=True, null=True)
    addinfo = models.CharField(db_column='AddInfo', max_length=200, blank=True, null=True)
    bankimportid = models.IntegerField(db_column='BankImportID', blank=True, null=True)
    statusid = models.SmallIntegerField(db_column='StatusID')
    userid = models.IntegerField(db_column='UserID')
    handletime = models.DateTimeField(db_column='HandleTime')

    class Meta:
        managed = False
        db_table = 'Transactions'


class Transationpatterns(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    typeid = models.SmallIntegerField(db_column='TypeID')
    categoryid = models.SmallIntegerField(db_column='CategoryID')
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)
    orderid = models.IntegerField(db_column='OrderID')
    imageid = models.IntegerField(db_column='ImageID', blank=True, null=True)
    levelid = models.SmallIntegerField(db_column='LevelID')
    formwidth = models.IntegerField(db_column='FormWidth', blank=True, null=True)
    formheight = models.IntegerField(db_column='FormHeight', blank=True, null=True)
    aftersql = models.CharField(db_column='AfterSQL', max_length=-1, blank=True, null=True)
    statusid = models.SmallIntegerField(db_column='StatusID')
    userid = models.IntegerField(db_column='UserID')
    handletime = models.DateTimeField(db_column='HandleTime')

    class Meta:
        managed = False
        db_table = 'TransationPatterns'


class Userpartitions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')
    partitionid = models.ForeignKey(Partitions, models.DO_NOTHING, db_column='PartitionID', blank=True, null=True)
    isprimary = models.TextField(db_column='IsPrimary', blank=True, null=True) This field type is a guess.

    class Meta:
        managed = False
        db_table = 'UserPartitions'
        unique_together = (('userid', 'partitionid'),)


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    login = models.CharField(db_column='Login', unique=True, max_length=200)
    password = models.CharField(db_column='Password', max_length=50)
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)
    isadmin = models.TextField(db_column='IsAdmin', blank=True, null=True) This field type is a guess.
    statusid = models.SmallIntegerField(db_column='StatusID')

    class Meta:
        managed = False
        db_table = 'Users'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
