# Generated by Django 2.1.5 on 2019-02-11 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0006_auto_20190211_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='type',
            field=models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.SET_NULL, to='funds.ClientType'),
        ),
    ]