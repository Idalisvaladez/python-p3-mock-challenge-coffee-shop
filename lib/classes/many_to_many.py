class Coffee:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            print("Coffee name cannot be changed.")
        elif isinstance(name, str) and len(name) >= 3:
            self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        # faster way return list(set([order.customer for order in Order.all if order.coffee == self]))
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        average = sum(prices) / len(prices)
        return average

class Customer:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    # @classmethod
    # def most_aficionado(cls, coffee):
    #     #getting all coffee orders
    #     coffee_orders = [order for order in Order.all if order.coffee == coffee]
    #     coffee_dict = {}
    #     #iterating over all orders of current coffee
    #     #iterating over all orders
    #     #find matching orders based on customer
    #     for coffee_order in coffee_orders:
    #         #iterating over Order.all and suming the orders.price where the
    #         # current order's customer matches the current coffee order
    #         coffee_dict[coffee_order.customer] = sum([orders.price for orders in Order.all if orders.customer == coffee_order.customer and orders.coffee == coffee])
    #     return max(coffee_dict, key=lambda x: coffee_dict[x])
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if hasattr( self, "price"):
            print("Sorry! The price cannot be changed.")
        elif isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee