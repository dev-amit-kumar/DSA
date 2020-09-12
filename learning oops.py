class School:

    def __init__(self, name, age, rollno, std):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.std = std
    
    def mark_attendance(self):
        print("student ", self.name, "is marking his attenance")
        print("student ", self.name, "marked successfully")
    
    def getData(self):
        print("Name = ",self.name)
        print("Age = ",self.age)
        print("Roll no = ",self.rollno)
        print("Std = ",self.std)

if __name__ == "__main__":
    student1 = School("Ayushi Verma", 24, 1, 12)
    # student2 = School("ABC", 24, 2, 12)
    # print(student1.name)
    # student1.mark_attendance()
    # student1.getData()
    # fees = 1500
    # student1.submitFees(fees)
    # student2.mark_attendance()
    # objName = className() -> this is a way to make a new object and inside bracket we can send the values of that obj

