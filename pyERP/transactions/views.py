from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import permissions
from django.shortcuts import render
from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
from .models import Transaction, Client, Currency
from .serializers import TransactionSerializers, ClientSerializers, CurrencySerializers

def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    return render(request, "index.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


class CurrencyAPI(APIView):
    def get(self,request):
        queryset = Currency.objects.all()
        serializer = CurrencySerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

class TransactionListView(ListView):
    template_name = 'transactions/transaction_list.html'
    queryset = Transaction.objects.all()

class TransactionAPI(APIView):
    def get(self,request):
        queryset = Transaction.objects.all()
        # queryset = Transaction.objects.filter(db_client_id = 0)
        serializer = TransactionSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

class ClientListView(ListView):
    template_name = 'client/client_list.html'
    queryset = Client.objects.all()

class ClientAPI(APIView):
    def get(self,request):
        queryset = Client.objects.all()
        serializer = ClientSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
