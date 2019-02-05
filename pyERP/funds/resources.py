from tastypie.resources import ModelResource
from .models import Currency
from tastypie.authorization import Authorization


class CurrencyResource(ModelResource):
    class Meta:
        queryset = Currency.objects.all()
        resource_name = 'currency'
        authorization = Authorization()