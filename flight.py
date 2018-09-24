MAX_ROWS = 25
MIN_ROWS = 1
MAX_SEATS = 6


class Flight:
    def __init__(self, flight_no, new_date, new_origint, new_dest, new_price):
        self.__flight_number = flight_no
        self.__date = new_date
        self.__origin = new_origint
        self.__destination = new_dest
        self.__price = new_price
        self.__seats_taken = []
        for i in range(0, MAX_ROWS * MAX_SEATS):
            self.__seats_taken.append('O')
            
    def get_flight_number(self):
        return self.__flight_number

    def get_date(self):
        return self.__new_date

    def get_origin(self):
        return self.__origin

    def get_destination(self):
        return self.__destination

    def get_price(self):
        return self.__price

    def assign_seat(self,new_seat):
        seat_details = str(new_seat)
        if len(seat_details) == 3:
            seat_num = int(seat_details[:2])
            if not (seat_num > 0 and seat_num < 26):
                print("Seat Row is invalid. Must be in rows 1-25.")
                return False
            else:
                seat_letter = seat_details[2:]
                if not (seat_letter == 'A' or seat_letter == 'B' or seat_letter == 'C' or seat_letter == 'D' or seat_letter == 'E' or seat_letter == 'F'):
                    print("Seat position invalid. You must enter a seat assignment with letter A-F.")
                    return False
                else:
                    if seat_details in self.__seats_taken:
                        print('Seat has been taken already. Please select another.')
                        return False
                    else:
                        self.__seats_taken.append(seat_details)
                        return True
            
        elif len(seat_details) == 2:
            seat_num = int(seat_details[:1])
            if not (seat_num > 0 and seat_num < 26):
                print("Seat Row is invalid. Must be in rows 1-25.")
                return False
            else:
                seat_letter = seat_details[1:]
                if not (seat_letter == 'A' or seat_letter == 'B' or seat_letter == 'C' or seat_letter == 'D' or seat_letter == 'E' or seat_letter == 'F'):
                    print("Seat position invalid. You must enter a seat assignment with letter A-F.")
                    return False
                else:
                    if seat_details in self.__seats_taken:
                        print('Seat has been taken already. Please select another.')
                        return False
                    else:
                        self.__seats_taken.append(seat_details)
                        return True
        else:
            print("Invalid seat length. Format should be Number|Number|Letter or Number|Letter. (e.g. 22A or 5B)")

    def release_seat(self,current_seat):
        seat_details = str(current_seat)
        if seat_details in self.__seats_taken:
            self.__seats_taken.remove(seat_details)
            return True
        else:
            print('Invalid Entry.', seat_details, 'is not taken, thus it cannot be removed.')
            return False
    def display_seat_map(self):

        count = 1
        print('    A B C   D E F')
        for x in range(MAX_ROWS):
            #for seat A
            seat_check_a = str(count) + 'A'
            if seat_check_a in self.__seats_taken:
                seat_a = '-'
            else:
                seat_a = 'O'
            #for seat B    
            seat_check_b = str(count) + 'B'
            if seat_check_b in self.__seats_taken:
                seat_b = '-'
            else:
                seat_b = 'O'
            #for seat C
            seat_check_c = str(count) + 'C'
            if seat_check_c in self.__seats_taken:
                seat_c = '-'
            else:
                seat_c = 'O'
            #for seat D
            seat_check_d = str(count) + 'D'
            if seat_check_d in self.__seats_taken:
                seat_d = '-'
            else:
                seat_d = 'O'
            #for seat E
            seat_check_e = str(count) + 'E'
            if seat_check_e in self.__seats_taken:
                seat_e = '-'
            else:
                seat_e = 'O'
            #for seat F
            seat_check_f = str(count) + 'F'
            if seat_check_f in self.__seats_taken:
                seat_f = '-'
            else:
                seat_f = 'O'

            print(count,' ',seat_a,seat_b,seat_c,' ',seat_d,seat_e,seat_f)
            count += 1
        print("('O' = Available; '-' = Assigned)")


    def __str__(self):
        string = 'Flight Number: ' + str(self.__flight_number) + '\n'
        string += 'Flight Date: ' + str(self.__date) + '\n'
        string += 'Flight Origin: ' + str(self.__origin) + '\n'
        string += 'Flight Destination: ' + str(self.__destination) + '\n'
        string += 'Flight Price: $' + str(self.__price) + '\n'
        return string
