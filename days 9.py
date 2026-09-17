class Payment:

    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount
class CreditCardPayment(Payment):
    def pay(self):
        print(f"Paid {self.get_amount()} by credit card")

class CashPayment(Payment):
    def pay(self):
        print(f"Paid {self.get_amount()} by cash")



payments = [
    CreditCardPayment(100),
    CashPayment(200)
]

for payment in payments:
    payment.pay()