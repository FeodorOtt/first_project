# Generated by Django 2.1.4 on 2019-01-15 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pymain', '0006_auto_20190115_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactiontaxes',
            name='cr_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transaction_taxes_cr_client', to='pymain.Clients'),
        ),
        migrations.AlterField(
            model_name='transactiontaxes',
            name='db_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transaction_taxes_db_client', to='pymain.Clients'),
        ),
    ]
