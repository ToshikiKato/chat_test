from django.shortcuts import render
from django.views.generic.list import ListView
from chat_app.models import Ticket

# Create your views here.
class TicketList(ListView):
    template_name = 'chat_app/ticket_list.html'
    model = Ticket
    context_object_name = 'ticket_list'

    def get_queryset(self):
        ## ここに一旦チケット取得 ##
        return Ticket.objects.all().order_by('id')