class Order:  
    def __init__(self, customer, coffee, price):  
        """Initialize Order with a customer, coffee, and price."""  
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):  
            raise ValueError("Price must be a float between 1.0 and 10.0")  
        if not isinstance(customer, Customer):  
            raise ValueError("Order must have a valid Customer")  
        if not isinstance(coffee, Coffee):  
            raise ValueError("Order must have a valid Coffee")  

        self._customer = customer    
        self._coffee = coffee   
        self._price = price    

    @property  
    def price(self):  
        """Return the order's price."""  
        return self._price  

    @property  
    def customer(self):  
        """Return the customer object for this order."""  
        return self._customer  

    @property  
    def coffee(self):  
        """Return the coffee object for this order."""  
        return self._coffee  

    def __repr__(self):  
        return f"<Order(customer={self.customer.name}, coffee={self.coffee.name}, price={self.price})>"