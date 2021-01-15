"""  The purpose of the file"""


class ParkingGarage():
    pass

    def __init__(self, parking):
        self.parking = parking
        print(self.parking)

        parking_dict = {}


# 1 create takeTicket (andy)
# Req's: This should decrease the amount of tickets available by 1
        # This should decrease the amount of parkingSpaces available by 1

# parkingSpaces =


    def takeTicket(self, parking_dict):
        pass

# create tickets list or dictionary with tickets

# 2 payForParking
# Req's: Display an input that waits for an amount from the user and store it in a variable
        # If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
        # This should update the "currentTicket" dictionary key "paid" to True

    def payForParking(self):
        pass


# 3 leaveGarage
# Req's: If the ticket has been paid, display a message of "Thank You, have a nice day"
        # If the ticket has not been paid, display an input prompt for payment
        # Once paid, display message "Thank you, have a nice day!"
        # Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
        # Update tickets list to increase by 1 (meaning add to the tickets list)

    def leaveGarage(self):
        pass


# key represents lot#, value represents ticket
parking_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
print(parking_dict)


# parking1 represents the first parking spot spot instances for entire parking lot
parking1 = ParkingGarage(1)
"""
parking2 = ParkingGarage(2)
parking3 = ParkingGarage(3)
parking4 = ParkingGarage(4)
parking5= ParkingGarage(5)
parking6 = ParkingGarage(6)
parking7 = ParkingGarage(7)
parking8 = ParkingGarage(8)
parking9 = ParkingGarage(9)
parking10 = ParkingGarage(10)
"""
