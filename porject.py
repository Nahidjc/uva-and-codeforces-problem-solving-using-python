room_501={'501A':0,'501B':0,'501C':0,'501D':0}
room_502={'502A':0,'502B':0,'502C':0,'502D':0}
room_503={'503A':0,'503B':0}
room_504={'504A':0,'504B':0,'504C':0,'504D':0}
Available_room = [room_501, room_502, room_503, room_504]


#if user is an admin then add seat user will assign the seat number according to the student ID

while True:
    firstCondition=int(input("Press 1 for Seat Booking \n Press 2 for Seat Change \nPress 3 Seat Cancel \nSearch Room by Student Id "))
    if firstCondition==1:
        print("Which room you are booking")
        room = int(input("Press 1 for Room 501 \nPress 2 for Room 502 \nPress 3 for Room 503 \nPress 4 for Room 504\n"))
        roomNumber = Available_room[room - 1]
        i = 0
        roomKeys = []
        for key in roomNumber:
            print("Press {0} seat {1}".format(i + 1, key))
            roomKeys.append(key)
            i += 1
        seat = int(input())
        bookingSeat = roomKeys[seat - 1]

        if (roomNumber[roomKeys[seat - 1]] == 0):
            studentID = int(input("Enter Student ID: "))
            roomNumber[roomKeys[seat - 1]] = studentID

        else:
            print("Seat not Available")
    elif firstCondition==2:
        pass
    elif firstCondition==3:
        studentID = int(input("Enter Student id for seat cancel"))
        pass
    elif firstCondition==4:


        pass


    print(roomNumber)
    #if roomNumber