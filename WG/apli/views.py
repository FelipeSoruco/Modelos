from django.shortcuts import render, get_object_or_404
from .models import Client


def index_contact(request):
    all_clients = Client.objects.all()
    return render(request, 'apli/index_contact.html', {'all_clients': all_clients})


def detail_contact(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'apli/detail_contact.html', {'client': client})
