import mariadb

# Connect to mariadb database
conn = mariadb.connect(
    user="root",
    password="root",
    host="localhost",
    port=3306,
    database="sampleDb"
)

cur = conn.cursor()
conn.autocommit = True

try:
    cur.execute("CREATE TABLE employee (name VARCHAR(30), phone VARCHAR(10), age INTEGER, salary DOUBLE, city VARCHAR(100), dept VARCHAR(100));")
except Exception as y:
    print(y)

# Function to get user's input
def getUserInput():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    age = input("Enter age: ")
    salary = input("Enter salary: ")
    city = input("Enter city: ")
    dept = input("Enter department: ")
    return name, phone, age, salary, city, dept

# Insert data according to user's input
query = """INSERT INTO employee(name, phone, age, salary, city, dept) VALUES(%s, %s, %d, %d, %s, %s)"""
name, phone, age, salary, city, dept = getUserInput()
record = (name, phone, int(age), float(salary), city, dept)
cur.execute(query,record)

# Insert data directly
cur.execute("INSERT INTO employee(name, phone, age, salary, city, dept) VALUES ('Anmol', '7466363609', 24, 10000, 'Hyderabad', 'Digital Innovation'), ('Aman', '9087534262', 26, 12000, 'Bangalore', 'App Development'), ('Balbir', '8907652891', 26, 14000, 'Pune', 'IT Network')")

# Read data from table
cur.execute("SELECT * FROM Employee")
for (name, phone, age, salary, city, dept) in cur:
    print("Name:", name, "\nPhone:", phone, "\nAge:", age, "\nSalary:", salary, "\nCity:", city, "\nDept:", dept)
