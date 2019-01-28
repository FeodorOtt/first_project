from django.urls import path
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
    path('', TransactionListView.as_view(), name='transaction-list'),
    path('api/', TransactionAPI.as_view(), name='transaction-list-json'),
    path('client/', ClientListView.as_view(), name='client-list'),
    path('client/api/', ClientAPI.as_view(), name='client-list-json'),
    path('currency/api/', CurrencyAPI.as_view(), name='currency-list-json'),
    # path('create/', CourseCreateView.as_view(), name='courses-create'),
    # path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    # path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
    # path('<int:id>/delete/', CourseDeleteView.as_view(), name='courses-delete'),
]
