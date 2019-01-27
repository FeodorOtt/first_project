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
from .models import Transactions, Clients, Currency
from .serializers import TransactionsSerializers, ClientsSerializers, CurrencySerializers

def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    return render(request, "index.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


class ClientsListView(ListView):
    template_name = 'transactions/transaction_list.html'
    queryset = Clients.objects.all()

class ClientsAPI(APIView):
    def get(self,request):
        queryset = Clients.objects.all()
        serializer = ClientsSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

class ClientsListView(ListView):
    template_name = 'transactions/transaction_list.html'
    queryset = Clients.objects.all()

class CurrencyAPI(APIView):
    def get(self,request):
        queryset = Currency.objects.all()
        serializer = CurrencySerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

class TransactionsListView(ListView):
    template_name = 'transactions/transaction_list.html'
    queryset = Transactions.objects.all()

class TransactionsAPI(APIView):
    def get(self,request):
        queryset = Transactions.objects.all()
        serializer = TransactionsSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
