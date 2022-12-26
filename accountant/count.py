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

#####
631pm 12/25/2022

Updating v1. Adding spaces fires the else condition in the for loop that prompts to the user
that he/she is typing the payment wrong. The if condition can't find a match from whitespace.
Will add an elif condition to handle whitespace.

643pm
Updated. Now to figure out how to handle the float problem. Sometimes I get answers that include 13 decimal places
to the right.

651pm
Added round functions in the match case block. round(value, digits after decimal pt ). Hope it works. Do I import
the math library?

Not working.

740pm
Solved the problem. Didnt need the round functions at all. Inside the match cases, take the string input and make
that into a float. Then multiply by 100 to get rid of the decimal point. Finally, when the for loop finishes
reading the file line by line, divide the total amount by 100 to bring the decimal point back.

v1.1 complete

"""
import re

f = open("billiam.txt", "r")    #only include txt file name if txt file is in same project folder

total = 0

for line in f:     #iterate each line from file

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
        
        match line[0]: #get first character for each line: +, -, or no sign
            case '+':
                total += float(line[1:]) * 100    #skip prefix if found. Then remove decimal point
            case '-':
                total -= float(line[1:]) * 100    #skip prefix if found. Then remove decimal point
            case _: 
                total += float(line) * 100       #Remove decimal point   
    
    elif re.compile(r"^\s$").findall(line):      #whitespace handling
        
        pass   #skip line and continue
    
    else:
        
        print(line + " is not a valid amount")
        
total /= 100    #back to decimal point
    
print("Total is: $" + format(total,".2f"))  #show total amount with 2 decimal points to the right

f.close() 

