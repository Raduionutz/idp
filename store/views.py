from django.shortcuts import render
from django.views.generic import ListView

from .models import Produs
# Create your views here.

def front(request):
    return render(request, 'store/index.html')

class ProdusList(ListView):
    model = Produs
    template_name = 'store/index.html'

    context_object_name = 'produse'
