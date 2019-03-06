from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from funds.views import index_view, about_view
from tastypie.api import Api

from funds.resources import CurrencyResource, ClientResource, TransactionResource, TransactionClientResource, TransactionDetailResource, TransactionDetailAccResource, \
    UserResource, PartitionResource, ClientCategoryResource, ClientCategoryLocaleResource, ClientTypeLocaleResource, ClientTypeResource, BankResource, \
    CountryResource, AccountResource, AccountTypeResource, AccountTypeLocaleResource, AccountCategoryResource, AccountCategoryLocaleResource, BalanceAccountResource, \
    AccountSaldoTypeResource, AccountPartitionResource

funds_api = Api(api_name='funds/api')
funds_api.register(UserResource())
funds_api.register(CurrencyResource())
funds_api.register(ClientResource())
funds_api.register(ClientTypeResource())
funds_api.register(ClientTypeLocaleResource())
funds_api.register(ClientCategoryResource())
funds_api.register(ClientCategoryLocaleResource())
funds_api.register(TransactionResource())
funds_api.register(TransactionClientResource())
funds_api.register(TransactionDetailResource())
funds_api.register(TransactionDetailAccResource())
funds_api.register(PartitionResource())
funds_api.register(BankResource())
funds_api.register(CountryResource())
funds_api.register(AccountResource())
funds_api.register(AccountSaldoTypeResource())
funds_api.register(AccountTypeResource())
funds_api.register(AccountTypeLocaleResource())
funds_api.register(AccountCategoryResource())
funds_api.register(AccountCategoryLocaleResource())
funds_api.register(AccountPartitionResource())
funds_api.register(BalanceAccountResource())

urlpatterns = [
    path('', index_view, name='index'),
    path('', include(funds_api.urls)),
    path('i18n/', include('django.conf.urls.i18n')),
    path('about/', about_view, name='about'),
    path('admin/', admin.site.urls, name='admin'),
    path('funds/', include('funds.urls')),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('accounts/', include("django.contrib.auth.urls")),
    # path('accounts/login/', views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
]
