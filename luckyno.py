# Python program showing 
# a use of input() to a funcion defined before

def message(name):
    number = len(name)R*3
    return print("Hello {}, your Lucky Number is {}.".format (name, number))

message (input("Please enter Your Name = "))