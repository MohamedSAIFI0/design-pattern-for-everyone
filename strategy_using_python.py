from abc import ABC, abstractclassmethod


#=============STRATEGY===================
class PayementStrategy(ABC):
    @abstractclassmethod
    def pay(self, amout):
        pass


#=============CONCRETE STRATGIES=========

class CreditCardPayment(PayementStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using credit card")


class PaypalPayment(PayementStrategy):
    def pay(self, amount):
        print(f"Paid {amount} Using paypal")

class BitcoinPayment(PayementStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Betcoin")


#====================Context================

class ShoppingCart:
    def __init__(self, payment_strategy: PayementStrategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)

#Client choisit la strategie

cart1 = ShoppingCart(CreditCardPayment())
cart1.checkout(100)

cart2 = ShoppingCart(PaypalPayment())
cart2.checkout(200)

cart3 = ShoppingCart(BitcoinPayment())
cart3.checkout(400)
        


