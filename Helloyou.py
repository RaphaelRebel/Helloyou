import datetime


#print (restart)
def restart(username):
    restart = input("%s, wil jij dit progamma nog een keer doen? Type Y/N: " %username).upper()
    if restart == "Y":
        main()
    elif restart == "N":
        print("Dankjewel")          
    else:
        print ("Verkeerde invoer, alleen Y of N")
        
    


def afspelen(username):  
    print('Hallo, %s.'%username)
    x = datetime.datetime.now()
    print("De datum en tijd is:")
    print(x)
    

def main():
    print ("Hello you!, ik ben Raphael.")
    print ("Wie ben jij?")
    username = input('Mijn naam is: ')
    afspelen(username)
    restart(username)

main()
