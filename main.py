from customer import Customer  
from coffee import Coffee  
from order import Order  

coffee1 = Coffee("Espresso")  
coffee2 = Coffee("Latte")  

customer1 = Customer("Alice")  
customer2 = Customer("Bob")  

order1 = customer1.create_order(coffee1, 5.0)  
order2 = customer1.create_order(coffee2, 6.0)  
order3 = customer2.create_order(coffee1, 4.5)  

print(customer1.orders)  
print(customer2.orders)  
print(customer1.coffees())