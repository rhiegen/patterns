import string
import random
from typing import List
from abc import ABC, abstractmethod

def generate_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase,k=length))

class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self,customer,issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self,list: List[SupportTicket]) -> List[SupportTicket]:
        pass

class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self,list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()

class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self,list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy

class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self,list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy



class customerSupport:
    tickets: List[SupportTicket] = []

    def createTicket(self, customer,issue):
        self.tickets.append(SupportTicket(customer,issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        #creating tickets
        ticket_list = processing_strategy.create_ordering(self.tickets)

        if len(ticket_list) == 0:
            print('there are no tickets')
            return
        
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self,ticket: SupportTicket):
        print('========================================')
        print(f'processing ticked id {ticket.id}')
        print(f'customer: {ticket.customer}')
        print(f'Issue: {ticket.issue}')
        print('========================================')

# creating application
app = customerSupport()

# register a few tickets
app.createTicket('John Smith', 'My computer makes strange sounds')
app.createTicket('Linus Torvalds', 'I need to create a good SO')
app.createTicket('Steve Jobbs', 'I will create an apparatus that I am going to name mobile phone')

# process the tickes
app.process_tickets(RandomOrderingStrategy())


