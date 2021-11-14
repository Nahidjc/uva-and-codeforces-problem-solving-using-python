class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class seat:
    def __init__(self,name):
        self.no = name
        self.ownby = None

    def add_holder(self,std):
        self.ownby = std

class hall:
    def __init__(self):
        self.seats = list()

    def add_seat(self,seat_no):
        self.seats.append(seat(seat_no))

    def add_student(self,std):
        for i in self.seats:
            if i.ownby == None:
                i.add_holder(std)
                print(i.no+" is booked by "+i.ownby.id)
                break

    def print_seats(self):
        for i in self.seats:
            print(i.no)
            if i.ownby == None:
                print("seat is free")
            else :
                print(i.ownby.name, i.ownby.id)




yksg = hall()
yksg.add_seat("501A")
yksg.add_seat("501B")
yksg.add_seat("501C")
yksg.add_seat("502A")
yksg.add_seat("502B")
yksg.add_seat("502C")
yksg.add_seat("503A")
yksg.add_seat("503B")
yksg.add_seat("504A")
yksg.add_seat("504B")
yksg.add_seat("504C")

for i in range(15):
    std_name = input("enter student Name: ")
    std_id = input("enter student ID: ")
    yksg.add_student(student(std_name,std_id))