from django.urls import path
from transactions.views import home_view
from .views import *
# (
#     # TransactionView,
#     TransactionListView,
#     # TransactionCreateView,
#     # TransactionUpdateView,
#     # TransactionDeleteView
# )

app_name = 'transactions'
urlpatterns = [
    path('', home_view, name='home'),
    path('transaction/', TransactionListView.as_view(), name='transaction-list'),
    path('transaction/api/', TransactionAPI.as_view(), name='transaction-list-json'),
    path('client/', ClientListView.as_view(), name='client-list'),
    path('client/api/', ClientAPI.as_view(), name='client-list-json'),
    path('currency/api/', CurrencyAPI.as_view(), name='currency-list-json'),
]
