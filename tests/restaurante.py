class Restaurante:
    def __init__(self, name, orders_in_the_queue=0):
        self.name = name
        if orders_in_the_queue >= 0:
            self.orders_in_the_queue = orders_in_the_queue
        else:
            raise ValueError('The number of orders in the queue must be greater than or equal to zero.')
        
        
    def add_order(self):
        self.orders_in_the_queue += 1
        
    def remove_order(self):
        if self.orders_in_the_queue > 0:
            self.orders_in_the_queue -= 1