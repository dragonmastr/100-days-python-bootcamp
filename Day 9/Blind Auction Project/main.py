import art
print(art.logo + "\n")
# TODO-1: Ask the user for input
a = {}
max_value= -9999999
namemax =""
flag = "yes"
while flag == "yes":
    name = str(input("What is your name?:"))
    bid = int(input("What is your bid?: $"))
    a[name] = bid
    flag = input("Are there any other bidders?").lower()
    print("\n"*100)

for key, value in a.items():
    if max_value < value:
        max_value = value
        namemax = key
print(f"the winner is {namemax}  with a bid of ${max_value}")

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


