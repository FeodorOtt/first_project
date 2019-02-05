from django.urls import path, include
# from funds.views import home_view
from .views import *
# (
#     # TransactionView,
#     TransactionListView,
#     # TransactionCreateView,
#     # TransactionUpdateView,
#     # TransactionDeleteView
# )

from .resources import CurrencyResource

currency_resource = CurrencyResource()
app_name = 'funds'

urlpatterns = [
    path('', index_view, name='index'),
    path('transaction/', TransactionListView.as_view(), name='transaction'),
    path('transaction/api/', TransactionAPI.as_view(), name='transaction-json'),
    path('client/', ClientListView.as_view(), name='client'),
    path('client/api/', ClientAPI.as_view(), name='client-json'),
    path('currency/', CurrencyListView.as_view(), name='currency'),
    path('api/', include(currency_resource.urls)),
    path('currency/api/', CurrencyAPI.as_view(), name='currency-json'),
    # path('currency/delete/<pk>/', CurrencyDeleteView.as_view(), name="currency-delete"),
    # path('currency/<pk>/', CurrencyUpdateView.as_view(), name="currency-update"),
]
