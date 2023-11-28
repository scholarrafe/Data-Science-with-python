def calculate():
    n = 5
    def square():
        nonlocal n
        return n*n
    return square

mynum = calculate()
print(mynum())
print(mynum())