print("Hi! My name is Shreyas. Welcome to my cafe! :)")
print("Would you like to buy a beverage? (y/n)")

bill  = 0
buy = input()

prices = [0,100,100,100,100,300,0]
items = ['','Mocha','Latte','Cocoa','Cappucino','Freakshake','']

range = 6

menu = '''

1. Mocha                        Rs. 100
2. Latte                        Rs. 100
3. Cocoa                        Rs. 100
4. Cappucino                    Rs. 150
5. A frickin freakshake         Rs. 300
6. Actually i did not want
   to purchase anything         Rs.0

'''

choice = ''

while(buy.upper() == 'Y' or buy.upper() == 'YES'):
    print("\nHere's the menu:")
    print(menu)
    print("Enter the number corresponding to the item you wish to purchase")

    choice = int(input())

    while(choice<1 or choice > range):
        print('Please enter a valid choice')
        choice = int(input())
    
    bill += prices[choice]

    if(prices[choice] != 0):
        print("Thanks for purchasing a ",items[choice],". It will be added to your bill.",sep='')
        print('Your current bill is',bill)
    
    print("\nWould you like to purchase another beverage? (y/n)")
    buy = input()

    buy = buy.upper()

    while(buy != "Y" and buy != 'N' and buy != 'YES' and buy != "NO"):
        print("Please enter 'y' or 'n'")
        buy = input().upper()
    
if(bill != 0):
    print("\nYour total bill is",bill)

print('Please visit again!')

    
    



