print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age =  int(input("what is your age"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adults price are $12")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo== 'y':
        bill += 3
else:
    print("Sorry you have to grow taller before you can ride.")
