from django.contrib import admin
from django.urls import path, include
from transactions.views import home_view, about_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('admin/', admin.site.urls),
    path('transaction/', include('transactions.urls')),
]
