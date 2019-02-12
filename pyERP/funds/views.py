# from rest_framework.views import APIView
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
# from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from rest_framework import permissions
from django.shortcuts import render
from django.views import View
# from django.urls import reverse_lazy
# from django.views.generic import (
#     CreateView,
#     DetailView,
#     ListView,
#     UpdateView,
#     ListView,
#     DeleteView
# )
from .models import Transaction, Client, Currency
# from .serializers import TransactionSerializers, ClientSerializers, CurrencySerializers

def index_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    return render(request, "index.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


@login_required
def currency_list_view(request, *args, **kwargs):
    return render(request, 'funds/currency_list.html', {})

@login_required
def bank_list_view(request, *args, **kwargs):
    return render(request, 'funds/bank_list.html', {})


@login_required
def client_list_view(request, *args, **kwargs):
    return render(request, 'funds/client_list.html', {})


@login_required
def transaction_list_view(request, *args, **kwargs):
    return render(request, 'funds/transaction_list.html', {})


# class TransactionListView(LoginRequiredMixin, ListView):
#     template_name = 'funds/transaction_list.html'
#     queryset = Transaction.objects.all()

# class TransactionAPI(LoginRequiredMixin, APIView):
#     def get(self,request):
#         queryset = Transaction.objects.all()
#         # queryset = Transaction.objects.filter(db_client_id = 0)
#         serializer = TransactionSerializers(queryset, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     def post(self, request, pk):
#         queryset = Transaction.objects.get(pk=pk)
#         data = JSONParser().parse(request)
#         serializer = TransactionSerializers(queryset, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)


