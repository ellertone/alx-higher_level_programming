class Customer:
    """
    A sample customer class.

    >>> customer_1 = Customer("John", "Brad", 1000)
    >>> customer_1.customer_mail()
    'John.Brad@email.com'
    >>> customer_1.customer_fullname()
    'John Brad'
    >>> customer_1.apply_discount()
    950
    """
    discount = 0.95

    def __init__(self, first, last, purchase):
        self.first = first
        self.last = last
        self.purchase = purchase

    def customer_mail(self):
        return f'{self.first}.{self.last}@email.com'

    def customer_fullname(self):
        return f'{self.first} {self.last}'

    def apply_discount(self):
        self.purchase = int(self.purchase * self.discount)
        return self.purchase

if __name__ == "__main__":
    import doctest
    doctest.testmod()
