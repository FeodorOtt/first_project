from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import permissions
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
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

def index_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    return render(request, "index.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


class CurrencyAPI(LoginRequiredMixin, APIView):
    def get(self,request):
        queryset = Currency.objects.all()
        serializer = CurrencySerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
        # return Response({"data": serializer.data})

    def post(self, request):
        currency = CurrencySerializers(data=request.data)
        if currency.is_valid():
            currency.save()
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})


class CurrencyListView(LoginRequiredMixin, ListView):
    template_name = 'funds/currency_list.html'
    queryset = Currency.objects.all()


class CurrencyDeleteView(LoginRequiredMixin, DeleteView):
    model = Currency
    success_url = reverse_lazy("funds:currency")

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)


class CurrencyUpdateView(LoginRequiredMixin,UpdateView):
    model = Currency
    fields = ('name', 'ISO_char',)

class TransactionListView(LoginRequiredMixin, ListView):
    template_name = 'funds/transaction_list.html'
    queryset = Transaction.objects.all()

class TransactionAPI(LoginRequiredMixin, APIView):
    def get(self,request):
        queryset = Transaction.objects.all()
        # queryset = Transaction.objects.filter(db_client_id = 0)
        serializer = TransactionSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, pk):
        queryset = Transaction.objects.get(pk=pk)
        data = JSONParser().parse(request)
        serializer = TransactionSerializers(queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

class ClientListView(LoginRequiredMixin, ListView):
    template_name = 'funds/client_list.html'
    queryset = Client.objects.all()

class ClientAPI(LoginRequiredMixin, APIView):
    def get(self,request):
        queryset = Client.objects.all()
        serializer = ClientSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
