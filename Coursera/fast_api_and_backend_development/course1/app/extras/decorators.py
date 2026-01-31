def fence(func):
    def wrapper():
        print("+"*10)
        func()
        print("+"*10)

@fence
def log():
    print("Logging")