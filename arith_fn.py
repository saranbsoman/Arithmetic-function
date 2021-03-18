#author : This program is written by saranbsoman in March 18, 2021

#Defining functions for arithmetic operations

# This function adds list of numbers
def add(items):
    total = 0
    for val in items:
        total = total + val
    return total

# This function subtracts list of numbers
def diff(items):
    if len(items) == 0:
        return (0)
    elif len(items) == 1:
        return (items[0])
    else:
        return (items[0] - sum(items[1:]))

# This function multiplies list of numbers
def multiply(items):
    total = 1
    for val in items:
        total = total * val
    return total

# This function divides two numbers
def divide(x,y):
    return x/y


# You can make a choice from given
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")

#take choice as input
choice = input("Enter choice(1/2/3/4/5): ")

#validates the choice
if choice in ['1','2','3']:
    num = int(input('How many numbers: '))
    print(num)

    lst = [] #name 'lst' is defined

    #enter value for 'n' iterations
    for n in range(num):
        while True:
            try:
                numbers = int(input('Enter number '))
                lst.append(numbers)
                break
            # display error for invalid inputs
            except ValueError:
                print("No valid integer! Please try again ...")


    if choice in ('1', '2', '3'):
        if choice == '1':
            print("Sum :", add(lst))

        elif choice == '2':
            print("Difference :", diff(lst))

        elif choice == '3':
            print("Product :", multiply(lst))

elif choice == '5':
    exit()

elif choice == '4':
    while True:
        try:
            a = int(input('Enter first number '))
            b = int(input('Enter second number '))
            print("Quotient :", divide(a,b))
            break
        except ValueError:
            print("No valid integer! Please try again ...")
else:
    print("Oops! Invalid Entry\nPlease select from given choice")

