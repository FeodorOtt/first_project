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

def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    return render(request, "index.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


class TransactionsListView(ListView):
    template_name = 'transactions/transactions_list.html'
    queryset = Transactions.objects.all() # <blog>/<modelname>_list.html
