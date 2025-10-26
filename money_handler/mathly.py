import math

def money_sorter(amount):
  
    print(f"Amount entered (in cents): ${amount}")
    
    hundreds = amount // 100  
    amount -= (hundreds * 100)

    print("Amount remaining after 100s:", amount)
    
    fifties = amount // 50 
    amount -= (fifties * 50) 

    print("Amount remaining after 50s:", amount)
    
    twenties = amount // 20 
    amount -= (twenties * 20) 

    print("Amount remaining after 20s:", amount)
    
    tens = amount // 10  
    amount -= (tens * 10) 
   
    print("Amount remaining after 10s:", amount)
    
    fives = amount // 5  
    amount -= (fives * 5) 
 
    print("Amount remaining after 5s:", amount)
    
    ones = amount // 1  
    amount -= (ones * 1) 
 
    print("Amount remaining after 1s:", amount)
    
    
    quarters = amount // .25  #floor division; no remainder
    amount -= (quarters * .25) #subtract the value of quarters from amount
  
    print("Amount remaining after quarters:", amount * 100)
    
    dimes = amount // .10
    amount -= (dimes * .10)
  
    print("Amount remaining after dimes:", amount * 100)
    
    nickels = amount // .05
    amount -= (nickels * .05)
  
    print("Amount remaining after nickels:", amount * 100)
    
    pennies = amount / .01
    
    #level out floating point imprecision
    if (pennies * .01) < .5:
        pennies = math.floor(pennies)
    else:
        pennies = math.ceil(pennies)
        
    print("100s:", hundreds)     
    print("50s:", fifties)
    print("20s:", twenties)
    print("10s:", tens)
    print("5s:", fives)
    print("1s:", ones)
    print("Quarters:", quarters)
    print("Dimes:", dimes)
    print("Nickels:", nickels)
    print("Pennies:", pennies)
    
    
def money_counter(hundred, fifty, twenty, ten, five, one, quarter, dime, nickel, penny):
    
    bill_100 = (hundred * 100)
    print(f"100s amount [{hundred}]: ${bill_100:.2f}")
    bill_50 = (fifty * 50)  
    print(f"50s amount [{fifty}]: ${bill_50:.2f}")
    bill_20 = (twenty * 20)
    print(f"20s amount [{twenty}]: ${bill_20:.2f}")
    bill_10 = (ten * 10)
    print(f"10s amount [{ten}]: ${bill_10:.2f}")
    bill_5 = (five * 5)
    print(f"5s amount [{five}]: ${bill_5:.2f}")
    bill_1 = (one * 1)
    print(f"1s amount [{one}]: ${bill_1:.2f}")
    
    
    q_coin = (quarter * 0.25)
    print(f"Quarter amount [{quarter}]: ${q_coin:.2f}")
    d_coin = (dime * 0.10)
    print(f"Dime amount [{dime}]: ${d_coin:.2f}")
    n_coin = (nickel * 0.05)
    print(f"Nickel amount [{nickel}]: ${n_coin:.2f}")
    p_coin = (penny * 0.01)
    print(f"Penny amount [{penny}]: ${p_coin:.2f}")


    bills = hundred + fifty + twenty + ten + five + one
    total_bills = bill_100 + bill_50 + bill_20 + bill_10 + bill_5 + bill_1
    print(f"Total bills amount [{bills}]: ${total_bills:.2f}")
    
    coins = quarter + dime + nickel + penny
    total_coins = q_coin + d_coin + n_coin + p_coin
    print(f"Total coins amount [{coins}]: ${total_coins:.2f}")
    
    print(f"Grand total amount: ${(total_bills + total_coins):.2f}")

def main():

    pick = 2 

    match(pick): 
        case 1:
            print("Enter amount in cents: ")
            amount = 32.67
            money_sorter(amount)
    
        case 2:
            print("Enter number of coins: ")
            hundred = 0;
            fifty = 0;  
            twenty = 0;
            ten = 0;
            five = 0;
            one = 0;
            quarter = 17;
            dime = 12;
            nickel = 9;
            penny = 117;
            money_counter(hundred, fifty, twenty, ten, five, one, quarter, dime, nickel, penny)

        case _:
            print("Invalid selection.")
    

if __name__ == "__main__":
    main()