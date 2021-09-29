# Task 4.7
# Implement a class Money to represent value and currency.
# You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
# Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency:
#
# exchange_rate = {
#     "EUR": 0.93,
#     "BYN": 2.1,
# }

# Example:
#
# x = Money(10, "BYN")
# y = Money(11) # define your own default value, e.g. “USD”
# z = Money(12.34, "EUR")
# print(z + 3.11 * x + y * 0.8) # result in “EUR”
# 543.21 EUR

# lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
# s = sum(lst)
# print(s) #result in “BYN”
# 123.45 BYN


#  Have a look at @functools.total_ordering

from functools import total_ordering


@total_ordering
class Money:
    exchange_rate = {'EUR': 0.93, 'BYN': 2.1, 'USD': 1, 'JPY': 100}

    def __init__(self, amount, currency="USD"):
        self.amount = float(amount)
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            result = self.amount + other
        else:
            result = self.amount + (other.amount * Money.exchange_rate[self.currency] / Money.exchange_rate[other.currency])
        return Money(result, self.currency)

    def __radd__(self, other):
        return Money(other + self.amount, self.currency)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            result = self.amount - other
        else:
            result = self.amount - other.amount / Money.exchange_rate[other.currency] * Money.exchange_rate[self.currency]
        return Money(result, self.currency)

    def __rsub__(self, other):
        return Money(other - self.amount, self.currency)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = self.amount * other
        else:
            result = self.amount * other.amount / Money.exchange_rate[other.currency] * Money.exchange_rate[self.currency]
        return Money(result, self.currency)

    def __rmul__(self, other):
        return Money(other * self.amount, self.currency)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            result = self.amount / other
        else:
            result = self.amount * Money.exchange_rate[other.currency] / other.amount
        return Money(result, self.currency)

    def __rtruediv__(self, other):
        return Money(other / self.amount, self.currency)

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.amount > other
        if isinstance(other, Money):
            if self.currency == other.currency:
                return self.amount < other.amount
            else:
                return self.amount / Money.exchange_rate[self.currency] < other.amount / Money.exchange_rate[other.currency]

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.amount < other
        if isinstance(other, Money):
            if self.currency == other.currency:
                return self.amount == other.amount
            else:
                return self.amount * Money.exchange_rate[self.currency] == other.amount * Money.exchange_rate[other.currency]


def main():
    x = Money(10, "BYN")
    y = Money(10) # define your own default value, e.g. “USD”
    z = Money(10, "EUR")

if __name__ == '__main__':
    main()

