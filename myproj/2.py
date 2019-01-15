# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accountclasses(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    innername = models.CharField(db_column='InnerName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountClasses'


class Accountgroups(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    innername = models.CharField(db_column='InnerName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountGroups'


class Accountpartitions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    accountid = models.ForeignKey('Accounts', models.DO_NOTHING, db_column='AccountID')  # Field name made lowercase.
    partitionid = models.ForeignKey('Partitions', models.DO_NOTHING, db_column='PartitionID')  # Field name made lowercase.
    isprimary = models.TextField(db_column='IsPrimary', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'AccountPartitions'
        unique_together = (('accountid', 'partitionid'),)


class Accountsaldotype(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountSaldoType'


class Accountsections(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    innername = models.CharField(db_column='InnerName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountSections'


class Accounttype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountType'


class Accounts(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=300)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    balanceaccountid = models.IntegerField(db_column='BalanceAccountID')  # Field name made lowercase.
    index = models.SmallIntegerField(db_column='Index')  # Field name made lowercase.
    saldotypeid = models.SmallIntegerField(db_column='SaldoTypeID')  # Field name made lowercase.
    typeid = models.SmallIntegerField(db_column='TypeID')  # Field name made lowercase.
    categoryid = models.SmallIntegerField(db_column='CategoryID', blank=True, null=True)  # Field name made lowercase.
    bankid = models.IntegerField(db_column='BankID', blank=True, null=True)  # Field name made lowercase.
    assignment = models.CharField(db_column='Assignment', max_length=300, blank=True, null=True)  # Field name made lowercase.
    begindate = models.DateField(db_column='BeginDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    parentclientid = models.IntegerField(db_column='ParentClientID', blank=True, null=True)  # Field name made lowercase.
    syncpartitionflag = models.TextField(db_column='SyncPartitionFlag', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    statusid = models.SmallIntegerField(db_column='StatusID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    handletime = models.DateTimeField(db_column='HandleTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Accounts'
        unique_together = (('number', 'clientid', 'balanceaccountid', 'index'),)


class Balanceaccounts(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    balancenumber = models.CharField(db_column='BalanceNumber', unique=True, max_length=4)  # Field name made lowercase.
    assignment = models.CharField(db_column='Assignment', max_length=200, blank=True, null=True)  # Field name made lowercase.
    innerassignment = models.CharField(db_column='InnerAssignment', max_length=200, blank=True, null=True)  # Field name made lowercase.
    saldotypeid = models.SmallIntegerField(db_column='SaldoTypeID')  # Field name made lowercase.
    typeid = models.SmallIntegerField(db_column='TypeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BalanceAccounts'


class Bankimport(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    linkedid = models.IntegerField(db_column='LinkedID', blank=True, null=True)  # Field name made lowercase.
    transactionpatternid = models.IntegerField(db_column='TransactionPatternID')  # Field name made lowercase.
    importdate = models.DateField(db_column='ImportDate')  # Field name made lowercase.
    filedate = models.DateField(db_column='FileDate')  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=255)  # Field name made lowercase.
    bankimportpatternid = models.IntegerField(db_column='BankImportPatternID')  # Field name made lowercase.
    isreverse = models.TextField(db_column='IsReverse', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dbcrid = models.TextField(db_column='DbCrID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    partitionid = models.IntegerField(db_column='PartitionID')  # Field name made lowercase.
    dbbankid = models.IntegerField(db_column='DbBankID', blank=True, null=True)  # Field name made lowercase.
    dbbanktextid = models.CharField(db_column='DbBankTextID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dbbankname = models.CharField(db_column='DbBankName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbaccountid = models.IntegerField(db_column='DbAccountID', blank=True, null=True)  # Field name made lowercase.
    dbaccountnumber = models.CharField(db_column='DbAccountNumber', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbclientid = models.IntegerField(db_column='DbClientID', blank=True, null=True)  # Field name made lowercase.
    dbclienttextid = models.CharField(db_column='DbClientTextID', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbclientname = models.CharField(db_column='DbClientName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    crbankid = models.IntegerField(db_column='CrBankID', blank=True, null=True)  # Field name made lowercase.
    crbanktextid = models.CharField(db_column='CrBankTextID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    crbankname = models.CharField(db_column='CrBankName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    craccountid = models.IntegerField(db_column='CrAccountID', blank=True, null=True)  # Field name made lowercase.
    craccountnumber = models.CharField(db_column='CrAccountNumber', max_length=300, blank=True, null=True)  # Field name made lowercase.
    crclientid = models.IntegerField(db_column='CrClientID', blank=True, null=True)  # Field name made lowercase.
    crclienttextid = models.CharField(db_column='CrClientTextID', max_length=300, blank=True, null=True)  # Field name made lowercase.
    crclientname = models.CharField(db_column='CrClientName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=15, decimal_places=2)  # Field name made lowercase.
    addamount = models.DecimalField(db_column='AddAmount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currencyid = models.IntegerField(db_column='CurrencyID', blank=True, null=True)  # Field name made lowercase.
    currencytextid = models.CharField(db_column='CurrencyTextID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    paymentdetails = models.CharField(db_column='PaymentDetails', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    addinfo = models.CharField(db_column='AddInfo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    statusid = models.SmallIntegerField(db_column='StatusID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    handletime = models.DateTimeField(db_column='HandleTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BankImport'


class Bankimportpatterns(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    fileformatid = models.SmallIntegerField(db_column='FileFormatID')  # Field name made lowercase.
    map = models.CharField(db_column='Map', max_length=-1)  # Field name made lowercase.
    skipfirstrows = models.IntegerField(db_column='SkipFirstRows', blank=True, null=True)  # Field name made lowercase.
    skipfirstcols = models.IntegerField(db_column='SkipFirstCols', blank=True, null=True)  # Field name made lowercase.
    delimiter = models.CharField(db_column='Delimiter', max_length=1, blank=True, null=True)  # Field name made lowercase.
    quote = models.CharField(db_column='Quote', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fileextentions = models.CharField(db_column='FileExtentions', max_length=100)  # Field name made lowercase.
    aftersql = models.CharField(db_column='AfterSQL', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    isresident = models.TextField(db_column='IsResident')  # Field name made lowercase. This field type is a guess.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    encodingid = models.SmallIntegerField(db_column='EncodingID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BankImportPatterns'


class Banks(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    textid = models.CharField(db_column='TextID', unique=True, max_length=300, blank=True, null=True)  # Field name made lowercase.
    countryid = models.SmallIntegerField(db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    contactdata = models.CharField(db_column='ContactData', max_length=300, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    handletime = models.DateTimeField(db_column='HandleTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Banks'


class Clientpartitions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.ForeignKey('Clients', models.DO_NOTHING, db_column='ClientID')  # Field name made lowercase.
    partitionid = models.ForeignKey('Partitions', models.DO_NOTHING, db_column='PartitionID')  # Field name made lowercase.
    isprimary = models.TextField(db_column='IsPrimary', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ClientPartitions'
        unique_together = (('clientid', 'partitionid'),)


class Clients(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500)  # Field name made lowercase.
    textid = models.CharField(db_column='TextID', max_length=300, blank=True, null=True)  # Field name made lowercase.
    typeid = models.SmallIntegerField(db_column='TypeID')  # Field name made lowercase.
    categoryid = models.SmallIntegerField(db_column='CategoryID', blank=True, null=True)  # Field name made lowercase.
    residentid = models.TextField(db_column='ResidentID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    responsibleclientid = models.IntegerField(db_column='ResponsibleClientID', blank=True, null=True)  # Field name made lowercase.
    documentid = models.SmallIntegerField(db_column='DocumentID', blank=True, null=True)  # Field name made lowercase.
    documentdata = models.CharField(db_column='DocumentData', max_length=300, blank=True, null=True)  # Field name made lowercase.
    contactdata = models.CharField(db_column='ContactData', max_length=300, blank=True, null=True)  # Field name made lowercase.
    addinfo = models.CharField(db_column='AddInfo', max_length=300, blank=True, null=True)  # Field name made lowercase.
    attractedby = models.ForeignKey('self', models.DO_NOTHING, db_column='AttractedBy', blank=True, null=True)  # Field name made lowercase.
    statusid = models.TextField(db_column='StatusID')  # Field name made lowercase. This field type is a guess.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    handletime = models.DateTimeField(db_column='HandleTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clients'


class Partitions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=200, blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    handletime = models.DateTimeField(db_column='HandleTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Partitions'


class Transactiondetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    transactionid = models.IntegerField(db_column='TransactionID')  # Field name made lowercase.
    orderid = models.SmallIntegerField(db_column='OrderID')  # Field name made lowercase.
    partitionid = models.IntegerField(db_column='PartitionID')  # Field name made lowercase.
    dbclientid = models.IntegerField(db_column='DbClientID')  # Field name made lowercase.
    dbaccountid = models.IntegerField(db_column='DbAccountID')  # Field name made lowercase.
    crclientid = models.IntegerField(db_column='CrClientID')  # Field name made lowercase.
    craccountid = models.IntegerField(db_column='CrAccountID')  # Field name made lowercase.
    currencyid = models.IntegerField(db_column='CurrencyID')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=15, decimal_places=2)  # Field name made lowercase.
    amount_e = models.DecimalField(db_column='Amount_E', max_digits=15, decimal_places=2)  # Field name made lowercase.
    statusid = models.SmallIntegerField(db_column='StatusID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    handletime = models.DateTimeField(db_column='HandleTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransactionDetails'
        unique_together = (('transactionid', 'orderid'),)


class Transactionpatternsfields(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    transactionpatternid = models.IntegerField(db_column='TransactionPatternID')  # Field name made lowercase.
    fieldtypeid = models.TextField(db_column='FieldTypeID')  # Field name made lowercase. This field type is a guess.
    taxorderid = models.SmallIntegerField(db_column='TaxOrderID', blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=100)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isreadonly = models.TextField(db_column='IsReadOnly', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    controlid = models.SmallIntegerField(db_column='ControlID')  # Field name made lowercase.
    width = models.SmallIntegerField(db_column='Width')  # Field name made lowercase.
    defaultvalue = models.CharField(db_column='DefaultValue', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    isrequired = models.TextField(db_column='IsRequired', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fontstyle = models.SmallIntegerField(db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    fontcolor = models.SmallIntegerField(db_column='FontColor', blank=True, null=True)  # Field name made lowercase.
    dictionarysql = models.CharField(db_column='DictionarySQL', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    format = models.CharField(db_column='Format', max_length=50, blank=True, null=True)  # Field name made lowercase.
    left = models.SmallIntegerField(db_column='Left')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransactionPatternsFields'


class Transactionpatternsscheme(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    patternid = models.IntegerField(db_column='PatternID')  # Field name made lowercase.
    orderid = models.SmallIntegerField(db_column='OrderID')  # Field name made lowercase.
    dbaccountfieldid = models.SmallIntegerField(db_column='DbAccountFieldID', blank=True, null=True)  # Field name made lowercase.
    dbbalanceaccountid = models.IntegerField(db_column='DbBalanceAccountID', blank=True, null=True)  # Field name made lowercase.
    dbaccountindex = models.SmallIntegerField(db_column='DbAccountIndex', blank=True, null=True)  # Field name made lowercase.
    dbaccounttypeid = models.SmallIntegerField(db_column='DbAccountTypeID', blank=True, null=True)  # Field name made lowercase.
    dbaccountcategoryid = models.SmallIntegerField(db_column='DbAccountCategoryID', blank=True, null=True)  # Field name made lowercase.
    dbclientfieldid = models.SmallIntegerField(db_column='DbClientFieldID', blank=True, null=True)  # Field name made lowercase.
    dbclientid = models.IntegerField(db_column='DbClientID', blank=True, null=True)  # Field name made lowercase.
    craccountfieldid = models.SmallIntegerField(db_column='CrAccountFieldID', blank=True, null=True)  # Field name made lowercase.
    crbalanceaccountid = models.IntegerField(db_column='CrBalanceAccountID', blank=True, null=True)  # Field name made lowercase.
    craccountindex = models.SmallIntegerField(db_column='CrAccountIndex', blank=True, null=True)  # Field name made lowercase.
    craccounttypeid = models.SmallIntegerField(db_column='CrAccountTypeID', blank=True, null=True)  # Field name made lowercase.
    craccountcategoryid = models.SmallIntegerField(db_column='CrAccountCategoryID', blank=True, null=True)  # Field name made lowercase.
    crclientfieldid = models.SmallIntegerField(db_column='CrClientFieldID', blank=True, null=True)  # Field name made lowercase.
    crclientid = models.IntegerField(db_column='CrClientID', blank=True, null=True)  # Field name made lowercase.
    amountsql = models.CharField(db_column='AmountSQL', max_length=-1)  # Field name made lowercase.
    currencyfieldid = models.SmallIntegerField(db_column='CurrencyFieldID', blank=True, null=True)  # Field name made lowercase.
    currencyid = models.IntegerField(db_column='CurrencyID', blank=True, null=True)  # Field name made lowercase.
    partitionid = models.IntegerField(db_column='PartitionID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    handletime = models.DateTimeField(db_column='HandleTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransactionPatternsScheme'
        unique_together = (('patternid', 'orderid'),)


class Transactiontaxes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    transactionid = models.IntegerField(db_column='TransactionID')  # Field name made lowercase.
    orderid = models.SmallIntegerField(db_column='OrderID')  # Field name made lowercase.
    dbclientid = models.IntegerField(db_column='DbClientID', blank=True, null=True)  # Field name made lowercase.
    crclientid = models.IntegerField(db_column='CrClientID', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    ratemethodid = models.SmallIntegerField(db_column='RateMethodID', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=15, decimal_places=2)  # Field name made lowercase.
    amount_e = models.DecimalField(db_column='Amount_E', max_digits=15, decimal_places=2)  # Field name made lowercase.
    statusid = models.SmallIntegerField(db_column='StatusID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    handletime = models.DateTimeField(db_column='HandleTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransactionTaxes'
        unique_together = (('transactionid', 'orderid'),)


class Transactions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    patternid = models.IntegerField(db_column='PatternID')  # Field name made lowercase.
    operdate = models.DateField(db_column='OperDate')  # Field name made lowercase.
    dbclientid = models.IntegerField(db_column='DbClientID')  # Field name made lowercase.
    dbaccountid = models.IntegerField(db_column='DbAccountID', blank=True, null=True)  # Field name made lowercase.
    crclientid = models.IntegerField(db_column='CrClientID')  # Field name made lowercase.
    craccountid = models.IntegerField(db_column='CrAccountID', blank=True, null=True)  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=15, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    exchangeincome = models.DecimalField(db_column='ExchangeIncome', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    partitionid = models.IntegerField(db_column='PartitionID')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=15, decimal_places=2)  # Field name made lowercase.
    amount_e = models.DecimalField(db_column='Amount_E', max_digits=15, decimal_places=2)  # Field name made lowercase.
    exchangeamount = models.DecimalField(db_column='ExchangeAmount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    exchangeamount_e = models.DecimalField(db_column='ExchangeAmount_E', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currencyid = models.IntegerField(db_column='CurrencyID')  # Field name made lowercase.
    exchangecurrencyid = models.IntegerField(db_column='ExchangeCurrencyID', blank=True, null=True)  # Field name made lowercase.
    paymentdetails = models.CharField(db_column='PaymentDetails', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    addinfo = models.CharField(db_column='AddInfo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bankimportid = models.IntegerField(db_column='BankImportID', blank=True, null=True)  # Field name made lowercase.
    statusid = models.SmallIntegerField(db_column='StatusID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    handletime = models.DateTimeField(db_column='HandleTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transactions'


class Transationpatterns(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    typeid = models.SmallIntegerField(db_column='TypeID')  # Field name made lowercase.
    categoryid = models.SmallIntegerField(db_column='CategoryID')  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID')  # Field name made lowercase.
    imageid = models.IntegerField(db_column='ImageID', blank=True, null=True)  # Field name made lowercase.
    levelid = models.SmallIntegerField(db_column='LevelID')  # Field name made lowercase.
    formwidth = models.IntegerField(db_column='FormWidth', blank=True, null=True)  # Field name made lowercase.
    formheight = models.IntegerField(db_column='FormHeight', blank=True, null=True)  # Field name made lowercase.
    aftersql = models.CharField(db_column='AfterSQL', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    statusid = models.SmallIntegerField(db_column='StatusID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    handletime = models.DateTimeField(db_column='HandleTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransationPatterns'


class Userpartitions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    partitionid = models.ForeignKey(Partitions, models.DO_NOTHING, db_column='PartitionID', blank=True, null=True)  # Field name made lowercase.
    isprimary = models.TextField(db_column='IsPrimary', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'UserPartitions'
        unique_together = (('userid', 'partitionid'),)


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', unique=True, max_length=200)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    isadmin = models.TextField(db_column='IsAdmin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    statusid = models.SmallIntegerField(db_column='StatusID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class VwTransactionstatuses(models.Model):
    id = models.SmallIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vw_transactionstatuses'
