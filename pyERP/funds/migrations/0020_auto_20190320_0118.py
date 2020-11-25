# Generated by Django 2.1.5 on 2019-03-20 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funds', '0019_auto_20190221_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountPartitionCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funds.Account')),
                ('partition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funds.Partition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='accountpartitioncart',
            unique_together={('user', 'account', 'partition')},
        ),
    ]