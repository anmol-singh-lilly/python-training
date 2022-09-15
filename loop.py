# for loop
cities = [
    'Delhi',
    'Bangalore',
    'Hyderabad',
    'Mumbai',
    'Pune'
]
print("Different Cities: ")
for city in cities:
    print(city)

# while loop
print("Multiples of 7 less than 100")
i = 1
while(i<100):
    if i%7 == 0:
        print(i)
    i = i+1