from django.db import models

# Create your models here.

# Ticket
class Ticket(models.Model):
    ticket_name = models.CharField('チケット名', max_length=255)

    def __str__(self):
        return self.ticket_name