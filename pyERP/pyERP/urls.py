from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from funds.views import index_view, about_view
from tastypie.api import Api

from funds.resources import CurrencyResource, ClientResource, TransactionResource

funds_api = Api(api_name='funds/api')
funds_api.register(CurrencyResource())
funds_api.register(ClientResource())
funds_api.register(TransactionResource())

urlpatterns = [
    path('', index_view, name='index'),
    path('', include(funds_api.urls)),
    path('about/', about_view, name='about'),
    path('admin/', admin.site.urls, name='admin'),
    path('funds/', include('funds.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
]
