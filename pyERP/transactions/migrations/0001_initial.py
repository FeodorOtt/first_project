# Generated by Django 2.1.5 on 2019-01-27 15:20

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('inner_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('inner_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('inner_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountPartitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=300)),
                ('balance_account', models.IntegerField()),
                ('index', models.SmallIntegerField()),
                ('category', models.SmallIntegerField(blank=True, null=True)),
                ('assignment', models.CharField(blank=True, max_length=300, null=True)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('sync_partition_flag', models.BooleanField(blank=True, null=True)),
                ('status_id', models.SmallIntegerField()),
                ('handle_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountSaldoTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_name', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountSections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('inner_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BalanceAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_number', models.CharField(max_length=4, unique=True)),
                ('assignment', models.CharField(blank=True, db_column='Assignment', max_length=500, null=True)),
                ('inner_assignment', models.CharField(blank=True, db_column='InnerAssignment', max_length=200, null=True)),
                ('saldo_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.AccountSaldoTypes')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.AccountTypes')),
            ],
        ),
        migrations.CreateModel(
            name='Bankimport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_date', models.DateField()),
                ('file_date', models.DateField()),
                ('file_name', models.CharField(max_length=255)),
                ('is_reverse', models.BooleanField(null=True)),
                ('db_cr_id', models.BooleanField(null=True)),
                ('db_bank_text_id', models.CharField(blank=True, max_length=200, null=True)),
                ('db_bank_name', models.CharField(blank=True, max_length=300, null=True)),
                ('db_account_number', models.CharField(blank=True, max_length=300, null=True)),
                ('db_client_text_id', models.CharField(blank=True, max_length=300, null=True)),
                ('db_client_name', models.CharField(blank=True, max_length=500, null=True)),
                ('cr_bank_text_id', models.CharField(blank=True, max_length=200, null=True)),
                ('cr_bank_name', models.CharField(blank=True, max_length=300, null=True)),
                ('cr_account_number', models.CharField(blank=True, max_length=300, null=True)),
                ('cr_client_text_id', models.CharField(blank=True, max_length=300, null=True)),
                ('cr_client_name', models.CharField(blank=True, max_length=500, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('add_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('currency_text_id', models.CharField(blank=True, max_length=100, null=True)),
                ('tax_date', models.DateField(blank=True, null=True)),
                ('payment_details', models.CharField(blank=True, max_length=1000, null=True)),
                ('add_info', models.CharField(blank=True, max_length=200, null=True)),
                ('status_id', models.SmallIntegerField()),
                ('handle_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BankImportPatterns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file_format_id', models.SmallIntegerField()),
                ('map', models.CharField(max_length=1000)),
                ('skip_first_rows', models.IntegerField(null=True)),
                ('skip_first_cols', models.IntegerField(null=True)),
                ('delimiter', models.CharField(blank=True, max_length=1, null=True)),
                ('quote', models.CharField(blank=True, max_length=1, null=True)),
                ('file_extentions', models.CharField(max_length=100)),
                ('after_sql', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_resident', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('encoding_id', models.SmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text_id', models.CharField(blank=True, max_length=300, null=True, unique=True)),
                ('country', models.SmallIntegerField(null=True)),
                ('contact_data', models.CharField(blank=True, max_length=300, null=True)),
                ('handle_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clientpartitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('text_id', models.CharField(blank=True, max_length=300, null=True)),
                ('type', models.SmallIntegerField()),
                ('category', models.SmallIntegerField(null=True)),
                ('is_resident', models.BooleanField(default=True)),
                ('document', models.SmallIntegerField(null=True)),
                ('document_data', models.CharField(blank=True, max_length=300, null=True)),
                ('contact_data', models.CharField(blank=True, max_length=300, null=True)),
                ('add_info', models.CharField(blank=True, max_length=300, null=True)),
                ('status_id', models.BooleanField()),
                ('handle_time', models.DateTimeField(auto_now=True)),
                ('attracted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attracted_by_client', to='transactions.Clients')),
                ('responsible_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients_responsible_client', to='transactions.Clients')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=5, null=True)),
                ('ISO_digit', models.CharField(max_length=3)),
                ('ISO_char', models.CharField(max_length=3)),
                ('status_id', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Partitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
                ('handle_time', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transactions.Clients')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.IntegerField()),
                ('order_id', models.SmallIntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('amount_e', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status_id', models.SmallIntegerField()),
                ('handle_time', models.DateTimeField(auto_now=True)),
                ('cr_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cr_account', to='transactions.Accounts')),
                ('cr_client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cr_client', to='transactions.Clients')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Currency')),
                ('db_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='db_account', to='transactions.Accounts')),
                ('db_client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='db_client', to='transactions.Clients')),
                ('partition', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Partitions')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionPatterns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.SmallIntegerField()),
                ('category', models.SmallIntegerField()),
                ('order_id', models.IntegerField()),
                ('icon_id', models.IntegerField(null=True)),
                ('level_id', models.SmallIntegerField()),
                ('form_width', models.IntegerField(null=True)),
                ('form_height', models.IntegerField(null=True)),
                ('after_sql', models.CharField(blank=True, max_length=1000, null=True)),
                ('status_id', models.SmallIntegerField()),
                ('handle_time', models.DateTimeField(auto_now=True)),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transactions.TransactionPatterns')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionPatternsFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_type_id', models.BooleanField()),
                ('tax_order_id', models.SmallIntegerField(null=True)),
                ('field_name', models.CharField(max_length=100)),
                ('caption', models.CharField(blank=True, max_length=100, null=True)),
                ('is_read_only', models.BooleanField(null=True)),
                ('control_id', models.SmallIntegerField()),
                ('width', models.SmallIntegerField()),
                ('defaultvalue', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_required', models.BooleanField(null=True)),
                ('font_style', models.SmallIntegerField(null=True)),
                ('font_color', models.CharField(max_length=50, null=True)),
                ('dictionary_sql', models.CharField(blank=True, max_length=1000, null=True)),
                ('format', models.CharField(blank=True, max_length=50, null=True)),
                ('left', models.SmallIntegerField()),
                ('transaction_pattern', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.TransactionPatterns')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionPatternsScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.SmallIntegerField(null=True)),
                ('db_account_index', models.SmallIntegerField(null=True)),
                ('cr_account_index', models.SmallIntegerField(null=True)),
                ('amount_sql', models.CharField(max_length=1000)),
                ('handle_time', models.DateTimeField(auto_now=True)),
                ('cr_account_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions_patterns_scheme_cr_account_category', to='transactions.AccountCategories')),
                ('cr_account_field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions_patterns_scheme_cr_account_field', to='transactions.TransactionPatternsFields')),
                ('cr_account_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions_patterns_scheme_cr_account_type', to='transactions.AccountTypes')),
                ('cr_balance_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions_patterns_scheme_cr_balance_account', to='transactions.BalanceAccounts')),
                ('cr_client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions_patterns_scheme_cr_client', to='transactions.Clients')),
                ('cr_client_field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions_patterns_scheme_cr_client_field', to='transactions.TransactionPatternsFields')),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='transactions.Currency')),
                ('currency_field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='transactions.TransactionPatternsFields')),
                ('db_account_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions_patterns_scheme_db_account_category', to='transactions.AccountCategories')),
                ('db_account_field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions_patterns_scheme_db_account_field', to='transactions.TransactionPatternsFields')),
                ('db_account_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions_patterns_scheme_db_account_type', to='transactions.AccountTypes')),
                ('db_balance_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions_patterns_scheme_db_balance_account', to='transactions.BalanceAccounts')),
                ('db_client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions_patterns_scheme_db_client', to='transactions.Clients')),
                ('db_client_field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions_patterns_scheme_db_client_field', to='transactions.TransactionPatternsFields')),
                ('partition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='transactions.Partitions')),
                ('pattern', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.TransactionPatterns')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oper_date', models.DateField()),
                ('currency_rate', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('exchange_income', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('amount_e', models.DecimalField(decimal_places=2, max_digits=15)),
                ('exchange_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('exchange_amount_e', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('payment_details', models.CharField(blank=True, max_length=1000, null=True)),
                ('addinfo', models.CharField(blank=True, max_length=200, null=True)),
                ('status_id', models.SmallIntegerField()),
                ('handle_time', models.DateTimeField(auto_now=True)),
                ('bankimport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transactions.Bankimport')),
                ('cr_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions_cr_account', to='transactions.Accounts')),
                ('cr_client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions_cr_client', to='transactions.Clients')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions_currency', to='transactions.Currency')),
                ('db_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions_db_account', to='transactions.Accounts')),
                ('db_client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions_db_client', to='transactions.Clients')),
                ('exchange_currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions_exchange_currency', to='transactions.Currency')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transactions.Transactions')),
                ('partition', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Partitions')),
                ('pattern', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='transactions.TransactionPatterns')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionTaxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.SmallIntegerField()),
                ('rate', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('rate_method', models.SmallIntegerField(null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('amount_e', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status_id', models.SmallIntegerField(null=True)),
                ('handle_time', models.DateTimeField(auto_now=True)),
                ('cr_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transaction_taxes_cr_client', to='transactions.Clients')),
                ('db_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transaction_taxes_db_client', to='transactions.Clients')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Transactions')),
            ],
        ),
        migrations.CreateModel(
            name='UserPartitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField(null=True)),
                ('partition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.Partitions')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UsersInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bria_name', models.CharField(max_length=100, null=True)),
                ('status_id', models.SmallIntegerField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transactions.Clients')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transactions.Users')),
            ],
        ),
        migrations.AddField(
            model_name='userpartitions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.Users'),
        ),
        migrations.AddField(
            model_name='transactiontaxes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Users'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='transactions.Users'),
        ),
        migrations.AddField(
            model_name='transactionpatternsscheme',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Users'),
        ),
        migrations.AddField(
            model_name='transactionpatterns',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Users'),
        ),
        migrations.AddField(
            model_name='transactiondetails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Users'),
        ),
        migrations.AddField(
            model_name='partitions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Users'),
        ),
        migrations.AddField(
            model_name='clients',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transactions.Users'),
        ),
        migrations.AddField(
            model_name='clientpartitions',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.Clients'),
        ),
        migrations.AddField(
            model_name='clientpartitions',
            name='partition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.Partitions'),
        ),
        migrations.AddField(
            model_name='banks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Users'),
        ),
        migrations.AddField(
            model_name='bankimport',
            name='bank_import_pattern',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.BankImportPatterns'),
        ),
        migrations.AddField(
            model_name='bankimport',
            name='cr_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bankimport_cr_account', to='transactions.Accounts'),
        ),
        migrations.AddField(
            model_name='bankimport',
            name='cr_bank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bankimport_cr_bank', to='transactions.Banks'),
        ),
        migrations.AddField(
            model_name='bankimport',
            name='cr_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bankimport_cr_client', to='transactions.Clients'),
        ),
        migrations.AddField(
            model_name='bankimport',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='transactions.Currency'),
        ),
        migrations.AddField(
            model_name='bankimport',
            name='db_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bankimport_db_account', to='transactions.Accounts'),
        ),
        migrations.AddField(
            model_name='bankimport',
            name='db_bank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bankimport_db_bank', to='transactions.Banks'),
        ),
        migrations.AddField(
            model_name='bankimport',
            name='db_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bankimport_db_client', to='transactions.Clients'),
        ),
        migrations.AddField(
            model_name='bankimport',
            name='linked_transaction_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.TransactionDetails'),
        ),
        migrations.AddField(
            model_name='bankimport',
            name='partition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.Partitions'),
        ),
        migrations.AddField(
            model_name='bankimport',
            name='transaction_pattern',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.TransactionPatterns'),
        ),
        migrations.AddField(
            model_name='bankimport',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Users'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.Banks'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.Clients'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='parent_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_client', to='transactions.Clients'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='saldo_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.AccountSaldoTypes'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.AccountTypes'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Users'),
        ),
        migrations.AddField(
            model_name='accountpartitions',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.Accounts'),
        ),
        migrations.AddField(
            model_name='accountpartitions',
            name='partition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.Partitions'),
        ),
        migrations.AlterUniqueTogether(
            name='userpartitions',
            unique_together={('user', 'partition')},
        ),
        migrations.AlterUniqueTogether(
            name='transactiontaxes',
            unique_together={('transaction', 'order_id')},
        ),
        migrations.AlterUniqueTogether(
            name='transactionpatternsscheme',
            unique_together={('pattern', 'order_id')},
        ),
        migrations.AlterUniqueTogether(
            name='transactiondetails',
            unique_together={('transaction', 'order_id')},
        ),
        migrations.AlterUniqueTogether(
            name='clientpartitions',
            unique_together={('client', 'partition')},
        ),
        migrations.AlterUniqueTogether(
            name='accounts',
            unique_together={('number', 'client', 'balance_account', 'index')},
        ),
        migrations.AlterUniqueTogether(
            name='accountpartitions',
            unique_together={('account', 'partition')},
        ),
    ]
