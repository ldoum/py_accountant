"""
Project made 203pm Christmas Eve Saturday

Got tired of calculating my past due water bills and fees by hand. I want to make a program
that reads a file with a long list of payments. Deposits and withdrawals. For simple
counting.

v1 - dumb accountant
+ prefix or no prefix: Deposits
- prefix: Withdrawals
Example:

+12.47  Deposit
45.78   Deposit
-6.82   Withdrawal


Core is script to add positive and negative numbers. Base number is 0.


227pm
Error thrown: TypeError: unsupported operand type(s) for +=: 'int' and '_io.TextIOWrapper'
Answer - https://astrofrog.github.io/py4sci/_static/08.%20Reading%20and%20writing%20files.html
    variable f thats assigned to file open func is a file handle. file open func is just
    returning an accessible object.

    for line in f:
        print(repr(line)) #shows contents line by line in strings; includes \n chars

        #str(line) works too. Doesn't show \n characters. Use this.

        #int(line) doesn't work.

Additions:
Filter out + and - . Integers only

406pm
I think the program worked. It returned $93.93.

45.67 + 45.78 + 5.89 - 3.41 = 93.93

The program works!

546pm
Broke the program. Got stuck on how my own code worked, because I copied and pasted some code from
the internet

552pm
Fixed.

1039pm
Importing regular expressions library for proper format

1103pm
Now I'm finished. Proper format established.

Actually, not done. Didn't take to account the amounts with 0 cents; no decimal point

1108pm
Updated.

1109pm
Final test passed. This program is ready now.

"""
import re

f = open("billiam.txt", "r") #only include txt file name if txt file is in same project folder

count = 0

for line in f: #iterate each line from file

    print(line.replace('\n',''))
    
    """
        only accept amounts in the format of 2 decimal pts ($456.78) or no decimal points ($87)
        this condition looks for amounts on each line that follow the format defined by this regex

        [\+\-]\d+\.\d{2}: +13.29 , -6.78, 

        \d+\.\d{2}: 45.98

        [\+\-]\d+: +12, -75

        \d+: 82
        
    """    
    if re.compile(r"^([\+\-]\d+\.\d{2}|\d+\.\d{2}|[\+\-]\d+|\d+)$").findall(line):
        
        match line[0]: #get first character for each line: +, -, or nothing
            case '+':
                count += float(line[1:]) #skip prefix if found
            case '-':
                count -= float(line[1:]) #skip prefix if found
            case _: 
                count += float(line)
    else:
        
        print(line + " is not a valid amount")
    
print("Total is: $" + str(count)) 
f.close() #finish

