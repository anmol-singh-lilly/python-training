import os

print(os.getcwd())
print(os.getpid())

# os.mkdir("./demoDirectory")
print(os.chdir("./demoDirectory"))
# os.rename("./demoDirectory", "./demoFolder")

print(os.getenv(key='Path'))

print(os.listdir())

print(os.walk(r"C://"))