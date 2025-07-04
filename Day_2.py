print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 ? \n"))
people = int(input("How many people to split the bill? \n"))
#we have used the PEMDAS rule to the calculation
amount = round(((bill * tip / 100) + bill) / round(people,2), 2)
#the f string is added and to get only 2 decimals we have used round(x,2)
print(f"Each person should pay : {amount}")
print("\nHave A Great Day")


