class AttainuAU16:
    attendance = 0

    def __init__(self, name, age, rollno, std):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.std = std

    def mark_attendance(self):
        print("student ", self.name, "is marking his attenance")
        print("student ", self.name, "marked successfully")
        self.attendance += 1

    def getData(self):
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("Roll no = ", self.rollno)
        print("Std = ", self.std)
        print("Total Attendance = ", self.attendance)


if __name__ == "__main__":
    student1 = AttainuAU16("Amit", 24, 1, 12)

    murgan = AttainuAU16("Murgan", 25, 12345, 'MERN STACK')
    murgan.mark_attendance()
    murgan.mark_attendance()
    murgan.mark_attendance()
    murgan.getData()

    amit = AttainuAU16("Amit", 25, 12345, 'MERN STACK')
    amit.mark_attendance()
    amit.mark_attendance()
    amit.mark_attendance()
    amit.getData()

    ankit = AttainuAU16("Ankit", 25, 12345, 'MERN STACK')
    ankit.mark_attendance()
    ankit.mark_attendance()
    ankit.mark_attendance()
    ankit.getData()


debbared student(which have less than 3 attendance)
if conditions -> logic


class Students:


class insturctor:
    attendance


class mentor:
    attendance
    check cc/asg
    check test
    check your project


class TA:
    attendance
    start sesion


encapsulation
