import random

while True:
    minimum_number = int(input("Enter the lower bound: "))
    maximum_number = int(input("Enter the upper bound: "))

    random_between = random.randint(minimum_number, maximum_number)
    print(random_between)