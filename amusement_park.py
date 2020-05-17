age = 12
print("\n\t\t\t\tIf Elif and Else statements")
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
print("\n\t\t same thing but set up so that only one print command for the criteria")
age = 500
if age <4:
    price = 0
elif age <18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

age = 12
if age <4:
    price=0
elif age < 18:
    price=5
elif age <65:
    price=10
elif age >65:
    price= 5

print ("your admission cost is $" + str(price)+ ".")
