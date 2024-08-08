
# creating a class to run a garage, the numbers of tickets, spaces, and if the user has paid or not 
class ParkingGarage():
    '''
    ParkingGarage must take ticket and parking space capacity
    Attributes tickets and parkingSpaces will be lists. 
    Attribute currentTicket is a dictionary

    '''
    #taking in ticket number, parking space number, and the dictionary is empty automatically
    def __init__(self, tickets, parkingSpaces, currentTicket = {}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces 
        self.currentTicket = {
            'paid': False,
        }

    # When this method is called, the amount of tickets and spaces decrease by 1
    def takeTicket(self): 
        self.tickets -= 1 
        self.parkingSpaces -= 1

    # this method will run when they want to pay for th parking ticket
    def payForParking(self):
        
        # ask the user how much they need to pay for the ticket. If empty it is assumed ticket is unpaid
        pay_amount = input("Enter the amount you paid for the ticket, leave empty if it is unpaid: ")

        # if user enters a value, then display ticket is paid, leave in 15 min. If Empty nothing happens. The value stays as False meaing it has not been paid 
        if len(pay_amount) != 0:
            print("Your ticket has been paid, you have 15 minutes to leave!")
            self.currentTicket['paid'] = True

    # this method will run when the user leaves the garage, checks if they have paid, if not they will ask them to enter amount to pay. 
    # once paid, the number of tickets and parkingSpaces increases by 1
    def leaveGarage(self):
        if self.currentTicket['paid'] == True: 
            print("Thank you, have a nice day")
            self.tickets += 1
            self.parkingSpaces += 1
        else:
            while self.currentTicket['paid'] == False:
                print("You have not paid")
                pay_amount = input("Enter the amount you must pay for the ticket: ")
                if len(pay_amount) != 0:
                    print("Thank you., have a nice day")
                    self.tickets += 1
                    self.parkingSpaces += 1
                    break


# Instantiating the ParkingGarage class
public_garage = ParkingGarage(20,20)

# This while loop runs when the user enters the garage and follows them until they quit.
def user_enter_garage():
    while True: 
        enter_garage = input("Do you want to take a ticket (yes/no): ")

        # if the user does enter the garage (yes) 
        if enter_garage.lower() == 'yes':
            public_garage.takeTicket()

            while True: 
                pay_ticket = input("Are you ready to leave the garage and pay for ticket (yes/ no): ")

                # if they do want to pay
                if pay_ticket.lower() == 'yes':
                    public_garage.payForParking()

                    # whether or not they enter an amount, the program will know if they did pay or not when they are actually leaving the garage
                    public_garage.leaveGarage()
                    break
                
                else: 
                    print("When you are ready to leave please come back to pay!")

        # if the user doesn't enter the garage (no), then the while loop will repeat    
        else: 
            print("You must enter yes if you want to take a ticket to enter garage")


user_enter_garage()