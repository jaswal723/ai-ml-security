# Medium: Write a script that attempts to open a file that doesn't exist. Catch the FileNotFoundError. 
# Use the finally block to print "Execution complete," proving the script didn't fatally crash.

try:
    with open("abc.txt",'r') as f:
        x = f.read()
except FileNotFoundError:
    print("File does not exist")
finally:
    print("Execution Complete")