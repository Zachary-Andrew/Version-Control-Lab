name = input("Enter your name : ")
age = int(input("Enter your age : "))
legal = 21
if age>=21:
    print(name, ", you are legal to drink!")
else:
    year = legal - age
    print(name, ", you are way too young! Just wait", year, "more years!")
