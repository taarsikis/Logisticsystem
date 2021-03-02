""" The main module """

import order
import vehicle
import item

class LogisticSystem:
    """ main class """
    def __init__(self, vehicles: list):
        """ values. """
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order_f):
        """ adds order to orders list if there is free vehicle """
        for this_vehicle in self.vehicles:
            if this_vehicle.isAvailable:
                self.orders.append(order_f)
                this_vehicle.isAvailable = False
                order_f.assignVehicle(this_vehicle)
                return
        print("There is no available vehicle to deliver an order.")

    def trackOrder(self,orderId) -> str:
        """ returns iformation about needed order """
        needed_order = 0
        for this_order in self.orders:
            if this_order.orderId == orderId:
                needed_order = this_order
                break
        if needed_order != 0:
            return f"Your order #{orderId} is sent to \
{needed_order.city}. Total price: {needed_order.calculateAmount()} UAH."
        return "No such order."

if __name__ == "__main__":
    vehicles = [vehicle.Vehicle(1), vehicle.Vehicle(2)]
    logSystem = LogisticSystem(vehicles)
    my_items = [item.Item('book',110), item.Item('chupachups',44)]
    my_order = order.Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
    print(my_order)
    logSystem.placeOrder(my_order)
    print(logSystem.trackOrder(1))


    my_items2 = [item.Item('flowers',11), item.Item('shoes',153), item.Item('helicopter',0.33)]
    my_order2 = order.Order('Andrii', 'Odessa', 3, my_items2)
    print(my_order2)
    # Your order number is 234976475.
    logSystem.placeOrder(my_order2)
    print(logSystem.trackOrder(2))

    my_items3 = [item.Item('coat',61.8), item.Item('shower',5070), item.Item('rollers',700)]
    my_order3 = order.Order("Olesya", 'Kharkiv', 17, my_items3)
    logSystem.placeOrder(my_order3)
    print(logSystem.trackOrder(4))
