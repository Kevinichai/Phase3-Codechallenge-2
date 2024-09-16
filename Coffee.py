class Coffee:  
    def __init__(self, name):  
        """Initialize Coffee with a name, ensuring it's valid."""  
        if not isinstance(name, str) or len(name) < 3:  
            raise ValueError("Coffee name must be a string of at least 3 characters")  
        self._name = name  
    @property  
    def name(self):  
        """Return the coffee's name."""  
        return self._name  

    def __repr__(self):  
        return f"<Coffee(name={self._name})>"  


# To store orders of each coffee  
coffee_orders = []