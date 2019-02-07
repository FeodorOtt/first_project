from django.urls import path, include
# from funds.views import home_view
from tastypie.api import Api
from .views import *
# (
#     # TransactionView,
#     TransactionListView,
#     # TransactionCreateView,
#     # TransactionUpdateView,
#     # TransactionDeleteView
# )

from .resources import CurrencyResource, ClientResourse, TransactionResourse

# funds_api = Api(api_name='funds')
# funds_api.register(CurrencyResource())
# funds_api.register(ClientResourse())
# funds_api.register(TransactionResourse())

currency_resource = CurrencyResource()
client_resource = ClientResourse()
transaction_resource = TransactionResourse()


app_name = 'funds'

urlpatterns = [
    path('', index_view, name='index'),
    path('transaction/', TransactionListView.as_view(), name='transaction'),
    path('transaction/api/', TransactionAPI.as_view(), name='transaction-json'),
    path('client/', client_list_view, name='client'),
    path('client/api/', ClientAPI.as_view(), name='client-json'),
    path('currency/', currency_list_view, name='currency'),
    path('currency/api/', CurrencyAPI.as_view(), name='currency-json'),
    # path('api/', include(funds_api.urls)),
    path('api/', include(currency_resource.urls)),
    path('api/', include(client_resource.urls)),
    path('api/', include(transaction_resource.urls)),
]
