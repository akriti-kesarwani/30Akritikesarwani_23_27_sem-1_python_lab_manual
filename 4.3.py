class ITM:
    count = 0
    def get(self):
        self.name = input("Enter the name of the student: ")
        self.age = int(input("Enter the age: "))
        self.dep = int(input("Enter the department (1 for B.Tech, 2 for PGDM): "))
        ITM.count += 1

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        if self.dep == 1:
            print("Department: B.Tech")
        elif self.dep == 2:
            print("Department: PGDM")
        print()


students = int(input("Enter the number of students: "))

btech_students = []
pgdm_students = []

for i in range(students):
    student = ITM()
    student.get()
    
    if student.dep == 1:
        btech_students.append(student)
    elif student.dep == 2:
        pgdm_students.append(student)

print("\nB.Tech Students:")
for student in btech_students:
    student.display()

print("\nPGDM Students:")
for student in pgdm_students:
    student.display()

print("\nTotal Admissions:", ITM.count)