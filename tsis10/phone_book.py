import csv
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="Shyngys1",
    database="postgres"
)
cur = conn.cursor()

Q1 = "CREATE TABLE Phonebook (id SERIAL PRIMARY KEY, name VARCHAR(50), number INT)"
Q2 = "INSERT INTO Phonebook (name, number) VALUES (%s, %s)"


way = int(input("console or file or update(0,1,2)?: "))

if way == 0:
    name = input("Name: ")
    number = int(input("Number: "))
    cur.execute(Q2, (name, number))
    conn.commit()
elif way == 2:
    id_num = input("Enter id: ")
    obj = input("Update name or number: ")
    if obj == "name":
        new = input("Enter new name: ")
        cur.execute("UPDATE Phonebook SET name = %s WHERE id = %s", (new, id_num))
    else:
        new = input("Enter new number: ")
        cur.execute("UPDATE Phonebook SET number = %s WHERE id = %s", (new, id_num))
    conn.commit()


cur.execute("SELECT table_schema FROM information_schema.tables WHERE table_name='Phonebook';")
print(cur)

cur.execute("SELECT * FROM Phonebook")
for x in cur:
    print(x)
