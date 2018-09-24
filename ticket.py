class Ticket:
    def __init__(self, new_ticket_no, new_name, new_flight_no, new_seat):
        self.__ticket_number = new_ticket_no
        self.__passenger_name = new_name
        self.__flight_number = new_flight_no
        self.__seat = new_seat

    def get_ticket_number(self):
        return self.__ticket_number

    def get_passenger_name(self):
        return self.__passenger_name

    def get_flight_number(self):
        return self.__flight_number

    def get_seat(self):
        return self.__seat

    def set_seat(self, new_seat):
        row = new_seat[:-1]
        return row

    def calc_price(self, base_price):
        seat = self.get_seat()
        if len(seat) == 3:
            row = int(seat[:2])
        elif len(seat) == 2:
            row = int(seat[:1])
        if row <= 3:
            price = base_price + (base_price * 2)

        elif row <= 10 and row >= 4:
            price = base_price + (base_price * 1.5)

        else:
            price = base_price

        return price

    def __str__(self):
        string = 'Ticket Number: ' + str(self.__ticket_number) + '\n'
        string += 'Passenger Name: ' + str(self.__passenger_name) + '\n'
        string += 'Flight Number: ' + str(self.__flight_number) + '\n'
        string += 'Seat Assignment: ' + str(self.__seat)
        return string
