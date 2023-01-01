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

"""
import re

f = open("billiam.txt", "r")    #only include txt file name if txt file is in same project folder

total = 0

for line in f:     #iterate each line from file

    transaction = line.replace('\n','') #remove newline characters and assign modded input to variable
    
    print(transaction)
    
    """
        only accept amounts in the format of 2 decimal pts ($456.78) or no decimal points ($87)
        this condition looks for amounts on each line that follow the format defined by this regex

        [\+\-]\d*\.\d{2}: +13.29 , -6.78, +.53

        \d*\.\d{2}: 45.98, .86

        [\+\-]\d+: +12, -75

        \d+: 82
        
    """    
    if re.compile(r"^([\+\-]\d*\.\d{2}|\d*\.\d{2}|[\+\-]\d+|\d+)$").findall(transaction):
        
        match transaction[0]: #get first character for each line: +, -, or no sign
            case '+':
                total += float(transaction[1:]) * 100    #skip prefix if found. Then remove decimal point
            case '-':
                total -= float(transaction[1:]) * 100    #skip prefix if found. Then remove decimal point
            case _: 
                total += float(transaction) * 100       #Remove decimal point   
    
    else: 
        
        pass   #skip line and continue
 
total /= 100    #back to decimal point
    
print(f"Total is: ${format(total,'.2f')}")  #show total amount with 2 decimal points to the right

f.close() 

