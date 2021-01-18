

# TICKET GENERATOR

# initialize the ticket
ticket = 0

# 5 parkings slots, key= parking slot, value = Occupied
parking_lot_spaces = (1, 2, 3, 4, 5)
parking_spaces = dict.fromkeys(parking_lot_spaces)
print()

parking_spaces = {1: False, 2: False, 3: False, 4: False, 5: False}

# has a ticket been issued?
print_ticket_state = False

# run until a ticket is issued (represents a user pulling up to request a ticket)
while print_ticket_state == False:

    ticket_response = input("Please type 'ticket' to request a ticket: ")

    # scenario: a ticket is being requested
    if ticket_response == "ticket":
        while v == False:
            if k, v in parking_spaces.items():
            if v == False:
                v == True
                parking_spaces.update({k: v})
                break

    else:
        print("Parking lot is full")

    print_ticket_state = True
    print(f"Current ticket: {ticket}")
    print(f"Current state: {print_ticket_state}")
    ticket += 1

    else:
        print("Ticket not requested")
