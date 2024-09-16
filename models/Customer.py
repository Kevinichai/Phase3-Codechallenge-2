class Customer:  
    customers = []  # List to hold instances of customers  

    def __init__(self, name):  
        """Initialize Customer with a name, ensuring it’s valid."""  
        if not isinstance(name, str) or not (1 <= len(name) <= 15):  
            raise ValueError("Customer name must be a string of 1 to 15 characters")  
        self._name = name  
        self.orders = []  # List to hold orders of the customer  
        Customer.customers.append(self)  # Store the customer instance  

    @property  
    def name(self):  
        """Return the customer's name."""  
        return self._name  

    def create_order(self, coffee, price):  
        """Create a new order associated with this customer and a coffee."""  
        new_order = Order(self, coffee, price)  
        self.orders.append(new_order)  
        coffee.orders.append(new_order)  
        return new_order  

    def coffees(self):  
        """Return unique list of coffees ordered by this customer."""  
        return {order.coffee for order in self.orders}  

    def __repr__(self):  
        return f"<Customer(name={self._name})>"  


# To store all orders of each customer  
customer_orders = []