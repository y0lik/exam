import time
import sqlite3

connection = sqlite3.connect("database.sl3", 5)

cur = connection.cursor()

cur.execute(f"CREATE TABLE Workers(Name TEXT, Age INTEGER, Position TEXT);")

cur.execute("INSERT INTO Workers (Name, Age, Position) VALUES ('John', 32, 'Director'), ('Andrei', 42, 'Marketing'), "
            "('Maryana', 34, 'Secretary'), ('Max', 25, 'Programmer');")



while True:
    try:
        inname=input(str("Write your name to login:\nMaryana\tMax\tAndrei\tJohn\n\n"))
        time.sleep(2)
        break
    except:
        print("You have to write your name.\n")

if inname !== "Maryana" or "Max" or "Andrei" or "John":
    print("Your name is not in the database.")
else:
    chooseact = input("I find your name in the database! What do you want to do with it?\n"
                      "\tDelete\tEdit\tSee\n")

if chooseact == "Delete":
    cur.execute("DELETE FROM Workers WHERE Name=inname;")





# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"You're {self.name}, "
#               f"your age is {self.age}.")
#
#
# class Worker(Human):
#     def __init__(self, position, salary, name, age):
#         super().__init__(name, age)
#         self.position = position
#         self.salary = salary
#
#     def infow(self):
#         print(f"You're work on {self.position}, "
#               f"your salary is {self.salary}.")
#
#
# class Student(Human):
#     def __init__(self, course, directionofcourse, name, age):
#         super().__init__(name, age)
#         self.course = course
#         self.directionofcourse = directionofcourse
#
#     def infos(self):
#         print(f"You're on the {self.course} of the {self.directionofcourse}.")
#
#
# h1 = Worker("director", "4500$", "Andrei", 32)
# h2 = Student("second", "medical course", "Katya", 20)
# h3 = Student("first", "legal course", "Sergei", 19)
# h4 = Worker("marketing department", "2600$", "Anna", 28)
#
#
# def password():
#     global choisepass
#     while True:
#         try:
#             choisepass = str(input("Enter your password:\n"))
#             break
#         except:
#             print("Only letters")
#
#
# print("Google company\nInfo storage\n\nLogin in\n")
#
# while True:
#     try:
#         choiseid = int(input("Select your ID:\nAndrei - 1\nKatya - 2\nSergei - 3\nAnna - 4\n"))
#         break
#     except:
#         print("Type 1, 2, 3 or 4\n")
#
# password()
#
# if choisepass != "admin":
#     print("Uncorrect password. Try again.")
#     time.sleep(1.5)
#     password()
# elif choisepass == "admin":
#     if choiseid == 1:
#         h1.info()
#         h1.infow()
#     elif choiseid == 2:
#         h2.info()
#         h2.infos()
#     elif choiseid == 3:
#         h3.info()
#         h3.infos()
#     elif choiseid == 4:
#         h4.info()
#         h4.infow()