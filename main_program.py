## NEW MAIN

import flight
import ticket
import random

FLIGHT_FILE = 'flights.txt'
TICKET_FILE = 'tickets.txt'
TICKET_INFORMATION = 'tickets-updated.txt'
PURCHASE_TICKET = 1
CANCEL_TICKET = 2
VIEW_TICKET = 3
VIEW_MAP = 4
CHANGE_SEAT = 5
EXIT = 6

def main():

    flight_dict = {}
    ticket_dict = {}

    process_flight(flight_dict)
    process_ticket(ticket_dict, flight_dict)
    print_menu()
    option = get_user_option()
    
    while option != EXIT:
        
        if option == PURCHASE_TICKET:
            purchase_tickets()
            
        elif option == CANCEL_TICKET:
            cancel_tickets()
                                    
        elif option == VIEW_TICKET:
            view_tickets()
                                    
        elif option == VIEW_MAP:
            view_map()

        elif option == CHANGE_SEAT:
            change_seat()

    #If EXIT write output           
    write_output(flight_dict, ticket_dict)
    
def process_flight(flight_dict):
    flight_info = open(FLIGHT_FILE, 'r')
    for flights in flight_info:
        flight_list = flights.rstrip('\n').split('^')
        flight_number = int(flight_list[0])
        flight_date = flight_list[1]
        flight_origin = flight_list[2]
        flight_destination = flight_list[3]
        flight_price = float(flight_list[4])
        my_flight = flight.Flight(flight_number, flight_date, flight_origin, flight_destination, flight_price)
        flight_dict[flight_number] = my_flight
    flight_info.close()

def process_ticket(ticket_dict, flight_dict):
    ticket_info = open(TICKET_FILE, 'r')
    for tickets in ticket_info:
        ticket_list = tickets.rstrip('\n').split('^')
        ticket_number = int(ticket_list[0])
        ticket_name = ticket_list[1]
        flight_number = int(ticket_list[2])
        ticket_seat_no = ticket_list[3]
        my_ticket = ticket.Ticket(ticket_number, ticket_name, flight_number, ticket_seat_no)
        ticket_dict[ticket_number] = my_ticket
        flight_dict[flight_number].assign_seat(ticket_seat_no)
    ticket_info.close()                      


def print_menu():
    print('1. Purchase ticket')
    print('2. Cancel ticket')
    print('3. View ticket')
    print('4. View seat map')
    print('5. Change seat')
    print('6. Done')

def get_user_option():
    option = int(input('What would you like to do? '))
    while option < PURCHASE_TICKET or option > EXIT:
        option = int(input('Invalid menu option. Please select again: '))
    return option


#Ticket Number^Passenger Name^Flight Number^Seat Number
def write_output(flight_dict, ticket_dict):
    ticket_info = open(TICKET_INFORMATION, 'w')
    for ticket in ticket_dict:
        my_ticket = ticket_dict[ticket]
        print(my_ticket)

def purchase_tickets():
    passenger_name = input('Please enter your name: ')
    flight_no = int(input('Please provide the flight number you would like to ride on: '))
    flight = flight_dict[flight_no]
    flight.display_seat_map()
    new_seat_number = input('Please enter an available seat on the flight: ')
    valid = flight.assign_seat(new_seat_number)
    price = ticket_dict[ticket_no].get_price()
    ticket_dict[ticket_no].calc_price(price)

    while not valid:
        new_seat_number = input('That seat is already taken or is not a valid seat number. Please enter an available seat on the flight: ')
        valid = flight.assign_seat(new_seat_number)
    new_ticket_number = random.randint(10000000, 99999999)

    while new_ticket_number in ticket_dict:
        new_ticket_number = random.randint(10000000, 99999999)

    my_ticket = ticket.Ticket(new_ticket_number, passenger_name, flight_no, new_seat_number)
    ticket_dict[new_ticket_number] = my_ticket

    print(' ')
    print('Your ticket has been purchased. Your ticket information is below')
    print(ticket_dict[new_ticket_number])
    print(flight_dict[flight_number])
    print(' ')
    print_menu()
    option = get_user_option()

def cancel_tickets():
    ticket_no = int(input('Please provide your ticket number: '))

    my_ticket = ticket_dict[ticket_no]
    flight = flight_dict[my_ticket.get_flight_number()]
    valid = flight.release_seat(my_ticket.get_seat())

    while not valid:
        ticket_no = int(input('That is not a valid ticket number. Please try again: '))
        valid = flight.release_seat(my_ticket.get_seat())
    del ticket_dict[ticket_no]

    print('Your ticket has been canceled. Please see our website so you can buy another ticket because we really want your money!')
    print(' ')
    print_menu()
    option = get_user_option()

def view_tickets():
    ticket_no = int(input('Please provide your ticket number: '))

    while ticket_no not in ticket_dict:
        ticket_no = int(input('That is not a valid ticket number. Please try again: '))

    print(ticket_dict[ticket_no])
    print(flight_dict[ticket_dict[ticket_no].get_flight_number()])
    print(' ')
    print_menu()
    option = get_user_option()

def view_map():
    flight_no = int(input('Please select your flight: '))
    flight = flight_dict[flight_no]
    flight.display_seat_map()
    print(' ')
    print_menu()
    option = get_user_option()

def change_seat():
    ticket_no = int(input('Please enter your ticket number: '))
    my_ticket = ticket_dict[ticket_no]
    flight = flight_dict[my_ticket.get_flight_number()]
    flight.display_seat_map()
    change_seat = input('Please enter an available seat on the flight: ')
    flight.release_seat(my_ticket.get_seat())
    valid = flight.assign_seat(change_seat)
    price = flight_dict[my_ticket.get_flight_number()].get_price()
    ticket_dict[ticket_no].calc_price(price)
    while not valid:
        change_seat = input('That seat is already taken or is not a valid seat number. Please enter an available seat on the flight: ')
        valid = flight.assign_seat(change_seat)

    my_ticket.set_seat(change_seat)

    print(' ')
    print_menu()
    option = get_user_option()
                                    
        


main()
