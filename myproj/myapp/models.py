from django.db import models

# Create your models here.
class account_classes(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    inner_name = models.CharField(db_column='InnerName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountClasses'
