from django.urls import path
from .views import *
# (
#     # TransactionsView,
#     TransactionsListView,
#     # TransactionsCreateView,
#     # TransactionsUpdateView,
#     # TransactionsDeleteView
# )

app_name = 'transactions'
urlpatterns = [
    path('', TransactionsListView.as_view(), name='transactions-list'),
    path('api/', TransactionsAPI.as_view(), name='transactions-list-json'),
    path('clients/', ClientsListView.as_view(), name='clients-list'),
    path('clients/api/', ClientsAPI.as_view(), name='clients-list-json'),
    # path('create/', CourseCreateView.as_view(), name='courses-create'),
    # path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    # path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
    # path('<int:id>/delete/', CourseDeleteView.as_view(), name='courses-delete'),
]
