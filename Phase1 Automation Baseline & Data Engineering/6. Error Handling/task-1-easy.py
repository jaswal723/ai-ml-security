# Easy: Write a script that asks the user for a number and divides 100 by that number. 
# Wrap it in a try/except block to catch a ZeroDivisionError and print a friendly warning instead of crashing.

print("We will divide 100 from the number you will enter")

while True:
    try:
        number = int(input("Enter a number - "))
    except:
        print("Please enter a valid number")
        continue
    else:
        break
 
try:
    result = 100/number
except ZeroDivisionError:
    print("Please use any other number than zero. 100 / 0 is not possible.")
else:
    print(f'100 / {number} = {result}')