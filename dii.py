import random
import string
from abc import ABC, abstractmethod
# dependency inversion and injection 

class Authorizer(ABC):
    @abstractmethod
    def authorize(self):
        '''Authorizes the user '''

    @abstractmethod
    def is_authorized(self)-> bool:
        """See if user is authorized"""

class Order:
    def __init__(self):
        self.id = ''.join(random.choices(string.ascii_lowercase,k=6))
        self.status = 'open'
    
    def set_status(self, status):
        self.status = status

class Authorizer_SMS(Authorizer):
    def __init__(self):
        self.authorized = False
        self.code = None

    def generate_sms_code(self):
        self.code = ''.join(random.choices(string.digits, k=6))
    
    def authorize(self):
        code = input('Enter SMS code: ')
        self.authorized = code == self.code

    def is_authorized(self) -> bool:
        return self.authorized

class PaymentProcessor:

    def __init__(self, authorizer: Authorizer):
        self.authorizer = authorizer

    def pay(self, order):
        self.authorizer.generate_sms_code()
        self.authorizer.authorize()
        if not self.authorizer.is_authorized():
            raise Exception('Not authorized')
        print(f'Processing payment for order {order.id}')
        order.set_status('paid')
        