requested_toppings = "sausage"
#if statement is checking if anchovies is the requested_toppings value.
#since it is not the requested topping the print statement is executed.
if requested_toppings !='anchovies':
    print("hold the anchovies!")
print("FYI THIS IS ALL 'IF' STATEMENTS")
answer = 17

if answer !=42:
    print('I defined the answer as 17, but if the answer is not equal to 42, then this statement prints.')

requested_toppings = ['mushrooms', 'extra cheese']

if 'muschrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding Pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished makin gyour pizza!")

requested_toppings = ['mushrooms', 'sausage', 'kale', 'green peppers', 'pepperoni', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print ("SORRY BRO, WE ARE OUT OF GREEN PEPPERS RN")
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
