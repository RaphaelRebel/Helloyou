print ("Hello you!, ik ben Raphael.")
print ("Wie ben jij?")
username = input('Mijn naam is: ')
print('Hallo, %s.'%username)

import datetime

x = datetime.datetime.now()

print("De datum en tijd is:")
print(x)

restart = input("%s, wil jij dit progamma nog een keer doen? Type Y/N: " %username)
#comment

if restart == "Y":
    print ("restart")
elif restart == "y":
    print("restart")
elif restart == "N":
    print("Dankjewel")
elif restart == "n":
    print("Dankjewel")    
    
else: print ("Verkeerde invoer, alleen Y of N")    
