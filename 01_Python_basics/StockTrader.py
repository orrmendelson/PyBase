# ##################################
class Stock:
    value = 0
    quantity = 0
    symbol = ""

    def __init__(self, symbol, quantity, value):
        self.symbol = symbol
        self.quantity = quantity
        self.value = value

    def get_total(self):
        return self.value * self.quantity

    def __str__(self):
        return "{} {} - total: {}".format(self.__class__.__name__, self.symbol, self.get_total())


# ##################################
class Bond(Stock):
    due_date = ""

    def __init__(self, symbol, quantity, value, date):
        Stock.__init__(self, symbol, quantity, value)
        self.due_date = date

    def get_due_date(self):
        return self.due_date

    def __str__(self):
        return "{}, due date: {}".format(super, self.get_due_date())


# ##################################
class Portfolio:
    stocks = []
    owner = None

    def add_stock(self, stock):
        self.stocks.append(stock)

    def get_total(self):
        total = 0
        for stock in self.stocks:
            total += stock.get_total()
        return total


# ##################################
class Customer:
    name = ""
    portfolios = []

    def __init__(self, name):
        self.name = name

    def add_portfolio(self, portfolio):
        self.portfolios.append(portfolio)

    def get_total(self):
        total = 0
        for portfolio in self.portfolios:
            total += portfolio.get_total()
        return total

    def __str__(self):
        return "{} total portfolios is {}".format(self.name, self.get_total())


# MAIN ##################################################
print("Stock Exe\n*******************")
stk1 = Stock("IBM", 15, 20)
stk2 = Stock("JnJ", 11, 55)
stk3 = Stock("BCG", 23, 10)
bnd1 = Bond("JamesBond", 40, 12, "2018-09-13")
print("{}\n{}\n{}\n{}".format(stk1, stk2, stk3, bnd1))

customer = Customer("Orr")
port1 = Portfolio()
port1.add_stock(stk1)
port1.add_stock(stk2)
customer.add_portfolio(port1)
print(customer)

port2 = Portfolio()
port2.add_stock(stk3)
customer.add_portfolio(port2)
print(customer)
port2.add_stock(bnd1)
print(customer)
