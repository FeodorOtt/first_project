from django.urls import path
# from funds.views import home_view
from .views import *
# (
#     # TransactionView,
#     TransactionListView,
#     # TransactionCreateView,
#     # TransactionUpdateView,
#     # TransactionDeleteView
# )

app_name = 'funds'

urlpatterns = [
    path('', index_view, name='index'),
    path('transaction/', TransactionListView.as_view(), name='transaction'),
    path('transaction/api/', TransactionAPI.as_view(), name='transaction-json'),
    path('client/', ClientListView.as_view(), name='client'),
    path('client/api/', ClientAPI.as_view(), name='client-json'),
    path('currency/', CurrencyListView.as_view(), name='currency'),
    path('currency/api/', CurrencyAPI.as_view(), name='currency-json'),
    path('currency/delete/<pk>/', CurrencyDeleteViev.as_view(), name="delete"),
]
