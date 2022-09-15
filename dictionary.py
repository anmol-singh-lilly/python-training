dt = {
    "name": "Anmol Singh",
    "contact": "7411599815",
    "email": "singh_anmol@lilly.com",
    "address": "Bangalore",
    "job-role": "Analyst - Software Configuration and Development",
}
print(dt)

del dt['job-role']
print(dt)

dt.update({"address": "Hyderabad"})
print(dt)

print(dt.keys())
print(dt.values())
