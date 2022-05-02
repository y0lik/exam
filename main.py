#                              Презентазація до екзамену Решетова Артемія
#Ця работа - "журнал", в якому знаходяться працівники компанії Google.
#Ти входиш в цей журнал, вписуючи своє ім'я (це зроблено для того, щоб якщо ти зробив шкоду для корпорації, то тебе
#могли легко знайти) Потім отримуєш дані про працивників та якщо твоє ім'я є в цьому списку то ти б міг з легкістю
#поміняти або ж видалити свої дані з цього списку, якщо там немає твого ім'я, ти можеш подиватись інфо про інших та вийти.

import time
import random
import sqlite3

nameedit = "a"
ageedit = 5
posedit = "c"

connection = sqlite3.connect("database.sl3", 5)

cur = connection.cursor()

# cur.execute(f"CREATE TABLE Workers(Name TEXT, Age INTEGER, Position TEXT);")

cur.execute("INSERT INTO Workers (Name, Age, Position) VALUES "
            "('John', 32, 'Director'), "
            "('Andrei', 42, 'Marketing'), "
            "('Maryana', 34, 'Secretary'), "
            "('Max', 25, 'Programmer');")

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Worker(Human):
    def __init__(self, position, name, age):
        super().__init__(name, age)
        self.position = position

    def infow(self):
        print(f"Name - {self.name}. Age - {self.age}. Position - {self.position}.")


class Student(Human):
    def __init__(self, form, name, age):
        super().__init__(name, age)
        self.form = form

    def infos(self):
        print(f"Name - {self.name}. Age - {self.age}. Form - {self.form}.")

maryana = Worker("Secretary", "Maryana", 34)
max = Worker("Programmer", "Max", 25)
andrei = Worker("Marketing", "Andrei", 42)
john = Worker("Director", "John", 32)


print("Hello! This is my exam project. Do you want to check it?\n")
time.sleep(1.5)
hello = input("Hmm? Y/N\n")

if hello == "Y":
    print("OK. Lets go!")
elif hello == "N":
    print("You have to check it!")
else:
    print("I don't care. You have to do it!")

print("\t\t\t\t GOOGLE\n\t\t\t\tDATABASE\n")

while True:
    try:
        inname=input(str("\t\tWrite your name to login:\n\n\tMaryana\t\tMax\t\tAndrei\t\tJohn\n\n"))
        time.sleep(1.5)
        break

    except:
        print("You have to write your name.\n")



if inname == "Maryana" or "Max" or "Andrei" or "John":
    print("Google database:")
    maryana.infow()
    max.infow()
    andrei.infow()
    john.infow()
    chooseact = input("\n\tI understand you! What do you want to do with database?\n"
                      "Delete my info(Delete)\tRandom edit my info(Random)\tClose app(Close)\n")

else:
    print("ERROR 404")



if chooseact == "Delete":
    time.sleep(1)
    print("Deleting successfully.\n\nGoogle 2022")

elif chooseact == "Random":
    acb = random.randint(1,3)
    if acb == 1:
        nameedit = "Denis"
        ageedit = 67
        posedit = "Director"

    elif acb == 2:
        nameedit = "Ben"
        ageedit = 45
        posedit = "Marketing"

    elif acb == 3:
        nameedit = "Bob"
        ageedit = 23
        posedit = "Secretary"



    print("Successfully.")
    time.sleep(1.2)
    print(f"\nYour new info:")
    time.sleep(0.8)
    print(f"\nName - {nameedit},"
          f"\nAge - {ageedit},"
          f"\nPosition - {posedit}.")
    time.sleep(1.4)
    print("\n\nGoogle 2022")

elif chooseact == "Close":
    print("OK. Closing..\nGoogle 2022")
    time.sleep(2)


connection.close()
