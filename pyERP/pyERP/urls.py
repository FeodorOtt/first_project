from django.contrib import admin
from django.urls import path, include
from funds.views import index_view, about_view

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('admin/', admin.site.urls),
    path('funds/', include('funds.urls')),
]
