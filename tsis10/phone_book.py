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
Q4 = "DELETE FROM Phonebook WHERE "

cur.execute("SELECT * FROM Phonebook")
for x in cur:
    print(x)


way = int(input("console-0, file-1, update-2, query-3, delete-4?: "))

if way == 0:
    name = input("Name: ")
    number = int(input("Number: "))
    cur.execute(Q2, (name, number))
    conn.commit()

elif way == 2:
    query = []
    print("Input column, column value, what to update, new value")
    for x in range(4):
        values = input()
        query.append(values)

    cur.execute(f"UPDATE Phonebook SET {query[2]} = %s WHERE {query[0]} = %s", (query[3], query[1]))
    conn.commit()

elif way == 3:
    query = []
    for x in range(2):
        values = input()
        query.append(values)
    cur.execute(f"SELECT * FROM Phonebook WHERE {query[0]} = %s", (query[1],))
    for x in cur:
        print(x)

elif way == 4:
    query = []
    for x in range(2):
        values = input()
        query.append(values)
    cur.execute(f"DELETE FROM Phonebook WHERE {query[0]} = %s", (query[1],))
    conn.commit()
else:
    quit()
