# https://rszalski.github.io/magicmethods/
class Transaction:
    def __init__(self, number, funds, status="active"):
        self.number = number
        self.funds = funds
        self.status = status
    
    def __repr__(self):
        return "Transaction({}, {})".format(self.number, self.funds)
    
    def __str__(self):
        return "Transaction {} for {} ({})".format(self.number, self.funds, self.status)

payment = Transaction("000001", 9999.999)
print(payment) # example of the output: <__main__.Transaction object at 0x11068f5f8>

payment = Transaction("000001", 9999.999)
print(payment)  # Transaction 000001 for 9999.999 (active)
print(repr(payment))  # Transaction(000001, 9999.999)