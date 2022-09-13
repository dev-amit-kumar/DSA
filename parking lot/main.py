class ParkingLot:
    def __init__(self, total_space):
        self.parking = {}
        self.total_car = 0
        self.total_slot = total_space
        for i in range(1, int(total_space)+1):
            self.parking[i] = []
        print("Created a parking lot with", total_space, "slots")

    def parkNewCar(self, regno, color):
        for key, values in self.parking.items():
            if values == []:
                values.append(regno)
                values.append(color)
                print("Allocated slot number: ", key)
                self.total_car += 1
                return
        print("Sorry, parking lot is full")

    def leaveCar(self, slot):
        if self.parking[int(slot)] != []:
            self.parking[int(slot)] = []
            print("Slot number", slot, "is free")
            self.total_car -= 1
        else:
            print("Slot number", slot, "is already free")

    def checkStatus(self):
        if self.total_car == 0:
            print("Parking Slot is Empty")
            return
        print("Slot No. Registration No Colour")
        for key, values in self.parking.items():
            if values != []:
                print(key, values[0], values[1])

    def findRegNobyColor(self, color):
        notFound = True
        for key, values in self.parking.items():
            if self.parking[key] != []:
                if self.parking[key][1] == color:
                    if notFound:
                        print(values[0], end="")
                        notFound = False
                    else:
                        print(",", values[0])
        if notFound:
            print("Not found")

    def findslotbycolor(self, color):
        notFound = True
        for key in self.parking:
            if self.parking[key] != []:
                if self.parking[key][1] == color:
                    if notFound:
                        print(key, end="")
                        notFound = False
                    else:
                        print(",", key)
        if notFound:
            print("Not found")

    def findslotbyreg(self, regno):
        for key, values in self.parking.items():
            if values != []:
                if values[0] == regno:
                    print(key)
                    return
        print("Not found")


if __name__ == "__main__":
    a = int(input("Press 1 for Interative commands & Press 2 for File Commands: "))
    if a == 1:
        while (True):
            take = input().split(" ")
            if take[0] == 'create_parking_lot':
                aa = ParkingLot(take[1])

            elif take[0] == 'park':
                aa.parkNewCar(take[1], take[2])

            elif take[0] == 'leave':
                aa.leaveCar(take[1])

            elif take[0] == 'status':
                aa.checkStatus()

            elif take[0] == 'registration_numbers_for_cars_with_colour':
                aa.findRegNobyColor(take[1])

            elif take[0] == 'slot_numbers_for_cars_with_colour':
                aa.findslotbycolor(take[1])

            elif take[0] == 'slot_number_for_registration_number':
                aa.findslotbyreg(take[1])

            elif take[0] == 'exit':
                break

            else:
                print("Wrong input")
    elif a == 2:
        input_file = open("file.txt", "r")
        all_input_lines = input_file.readlines()
        for input_line in all_input_lines:
            take = input_line.split(" ")
            if take[0] == 'create_parking_lot':
                aa = ParkingLot(take[1])

            elif take[0] == 'park':
                aa.parkNewCar(take[1], take[2])

            elif take[0] == 'leave':
                aa.leaveCar(take[1])

            elif take[0] == 'status':
                aa.checkStatus()

            elif take[0] == 'registration_numbers_for_cars_with_colour':
                aa.findRegNobyColor(take[1])

            elif take[0] == 'slot_numbers_for_cars_with_colour':
                aa.findslotbycolor(take[1])

            elif take[0] == 'slot_number_for_registration_number':
                aa.findslotbyreg(take[1])

            elif take[0] == 'exit':
                break

            else:
                print("Wrong input")
        input_file.close()
    else:
        print("Choose from 2 options only")
