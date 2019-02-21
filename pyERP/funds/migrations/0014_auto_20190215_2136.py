# Generated by Django 2.1.5 on 2019-02-15 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0013_clienttypelocale_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='short_name',
        ),
        migrations.AddField(
            model_name='currency',
            name='latin_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
