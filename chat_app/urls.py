from django.urls import path
from django.conf.urls import url
from chat_app import views

app_name = 'chat_app'
urlpatterns = [
    path('', views.TicketList.as_view(), name='ticket_list'),


]
