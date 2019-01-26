from rest_framework.views import APIView
from rest_framework.response import Response
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
from .models import Transactions
from .serializers import TransactionsSerializers

def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    return render(request, "index.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


class TransactionsListView(ListView):
    template_name = 'transactions/transaction_list.html'
    queryset = Transactions.objects.all()

class TransactionsAPI(APIView):
    def get(self,request):
        queryset = Transactions.objects.all()
        serializer = TransactionsSerializers(queryset, many=True)
        return Response(serializer.data)
