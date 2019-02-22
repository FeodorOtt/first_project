from django.urls import path, include
# from tastypie.api import Api
from .views import *
# (
#     # TransactionView,
#     TransactionListView,
#     # TransactionCreateView,
#     # TransactionUpdateView,
#     # TransactionDeleteView
# )

# from .resources import CurrencyResource, ClientResource, TransactionResource

# api = Api(api_name='api')
# api.register(CurrencyResource())
# api.register(ClientResource())
# api.register(TransactionResource())

# currency_resource = CurrencyResource()
# client_resource = ClientResource()
# transaction_resource = TransactionResource()


app_name = 'funds'

urlpatterns = [
    path('', index_view, name='index'),
    path('transaction/', transaction_list_view, name='transaction'),
    path('client/', client_list_view, name='client'),
    path('currency/', currency_list_view, name='currency'),
    path('bank/', bank_list_view, name='bank'),
    path('account/', account_list_view, name='account'),

    # path('currency/api/', CurrencyAPI.as_view(), name='currency-json'),
    # path('', include(api.urls), name='api'),
    # path('api/', include(currency_resource.urls)),
]
