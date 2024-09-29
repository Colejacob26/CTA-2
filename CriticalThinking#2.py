#Part 1
print("Please enter the meal price") 
mealPurchasePrice = int(input())
#Collects price for food

salesTax = .07
tipPercent = .18
#for tip and tax calculation


tax = round(mealPurchasePrice * salesTax,2)
tip = round(mealPurchasePrice * tipPercent,2)
total = mealPurchasePrice + tax + tip
#Calculations for adding tip and tax rounded by 2 decimals
#Total price with tip and tax included


print("Tax Amount:", tax)
print("Tip Amount:", tip)
print("Grand Total:", total)
#Prints out: tax, tip, then grand total


#Part 2
print("Please enter the current time in hours only (24Hours Clock)")
time = int(input())
print("Please enter how far to set the alarm in hours")
alarm = int(input())


totalHours = time + alarm
#Adds the time and alarm time to help the 24 hour conversion calculation below


#Check if we have past midnight with if statement
if totalHours > 24:
    temp = totalHours % 24
    # we use % as it will give us the remaining time after sorting through the amount of days
    print(temp)
#print out results for a new days time

elif totalHours == 24:
    temp = 0
    print(temp)
#Checks for midnight

else:
    print(totalHours)
#prints out results that dont pass the current day
    
    










