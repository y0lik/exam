import time

import sqlite3



connection = sqlite3.connect("database.sl3", 5)

cur = connection.cursor()

cur.execute(f"CREATE TABLE Workers(Name TEXT, Age INTEGER, Position TEXT);")

cur.execute("INSERT INTO Workers (Name, Age, Position) VALUES "
            "('John', 32, 'Director'), "
            "('Andrei', 42, 'Marketing'), "
            "('Maryana', 34, 'Secretary'), "
            "('Max', 25, 'Programmer');")



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
    cur.execute(f"DELETE FROM Workers WHERE Name={inname};")

elif chooseact == "Edit":
    nameedit = input("Write the name that you want to write? ")
    ageedit = input("Write the age that you want to write? ")
    posedit = input("Write the position that you want to write? ")
    cur.execute(f"DELETE FROM Workers WHERE Name={inname};")
    cur.execute(f"INSERT INTO Workers (Name, Age, Position) VALUES ({nameedit}, {ageedit}, {posedit})
    print("Successfully.")





connection.close()