# Generated by Django 2.1.5 on 2019-02-14 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0010_auto_20190212_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='latin_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
