""" This module foa class Order """


order_id = 0

class Order:
    """ Class for all types of orders """
    def __init__(self, user_name: str, city: str, postoffice : int, items: list):
        """ values. """
        global order_id
        order_id += 1
        self.orderId = order_id
        self.user_name = user_name
        self.items = items
        self.city = city
        self.postoffice = postoffice

    def __str__(self) -> str:
        """ will be returned after print """
        return f"Your order number is {self.orderId}"

    def calculateAmount(self) -> int:
        """ Returns amount of this order """
        amount = 0
        for item in self.items:
            amount += item.price
        return amount


    def assignVehicle(self, vehicle):
        """ Assigns a vehicle to this order """
        self.vehicle = vehicle
