import datetime


# print (restart)
# Bij Y restart het progamma
def restart(username):
    restart = input(" Of wil jij dit progamma nog een keer doen? Type Y/N: ").upper()
    if restart == "Y":
        main()
    elif restart == "N":
        print("Dankjewel")
    
    else:
        print("Verkeerde invoer, alleen Y of N")
        main()

#Hier is de introductie voor de vragen
def intro(username):
    print("Welkom! Dit is mijn progamma, maar niet mijn verhaal. Dit verhaal gaat over Salah en zijn gezin.")

# Vraag 1, Wat doe ik graag als hobby?
def vraag1():
    print("====================================================")
    print("PART 1")
    print("====================================================")
    print("Awadh, de zoon van Salah is allergisch voor bepaalde voedstoffen. Zijn moeder genaamd Mona, heeft de keuze om eten mee te nemen. Maar dat zou ze alleen moeten doen als ze hun eigen eten niet hier in Nederland zouden kunnen maken.")
    print("1. Wat doet Mona?")
    print("A: Ze neemt het eten mee")
    print("B: Om ruimte te besparen neemt ze het eten niet mee")
    vraag1 = input("Kies A of B: ").upper()
    if vraag1 == "A":
        print("Mona hoeft zich geen zorgen te maken over slechte voedingstoffen voor Awadh.")
        vraag2()
    elif vraag1 == "B":
        print("Mona moet zich zorgen maken over de slechte voedingstoffen voor Awadh.")
        vraag3()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag1()

def vraag2():
    print("====================================================")
    print("2. Het vliegtuig is geland, hoe heeft Awadh geslapen?")
    print("A: Goed")
    print("B: Slecht")
    vraag2 = input("Kies A of B: ").upper()
    if vraag2 == "A":
        print("Salah krijgt een stevige knuffel van zijn zoon, Awadh. Salah is een gelukkige man die weer samen is met zijn familie. Gelukkig is de vlucht goed gegaan.")
        vraag7()
    elif vraag2 == "B":
        print("Awadh heeft zich niet kunnen inhouden en is in paniek geslagen.")
        vraag4()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag2()

def vraag3():
    print("====================================================")
    print("3. Maakt Mona zich veel zorgen tijdens de vlucht over wat Awadh eet?")
    print("A: Ja")
    print("B: Nee")
    vraag3 = input("Kies A of B: ").upper()
    if vraag3 == "A":
        print("Mona heeft zichzelf niet goed gerust in het vliegtuig")
        vraag2()
    elif vraag3 == "B":
        print("Mona heeft goed gerust in het vliegtuig.")
        vraag2()
    else:
        print("Verkeerde invoer, alleen Y of N")
        main()

def vraag4():
    print("====================================================")
    print("4. Is Awadh gaan wegrennen terwijl Mona bezig was met de bagage?")
    print("A: Ja")
    print("B: Nee")
    vraag4 = input("Kies A of B: ").upper()
    if vraag4 == "A":
        print("Er word een kleine zoektocht gestart.")
        vraag5()
    elif vraag4 == "B":
        print("Bijna alles gaat weer goed. Salah is een gelukkige man die weer samen is met zijn gezin. Helaas was de vlucht niet zo goed gegaan.")
        vraag7()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag4()

def vraag5():
    print("====================================================")
    print("5. Word Awadh gevonden?")
    print("A: Ja")
    print("B: Nee")
    vraag5 = input("Kies A of B: ").upper()
    if vraag5 == "A":
        print("Na een grote schrik is Awadh weer gevonden. Gelukkig zijn ze nog optijd.")
        print("Gelukkig is het niet al te erg afgelopen. Salah is nu een gelukkige man met zijn gezin opweg naar het aziel.")
        vraag7()
    elif vraag5 == "B":
        print("Mona raakt ongelovelijk in de stress")
        vraag6()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag5()

def vraag6():
    print("====================================================")
    print("6. Wat doet Salah")
    print("A: Hij begint te schreeuwen op het vliegveld.")
    print("B: Hij gaat opzoek naar beveiliging.")
    vraag6 = input("Kies A of B: ").upper()
    if vraag6 == "A":
        print("Uren zijn voorbij. Awadh is nogsteeds niet gevonden en niemand weet waar hij zou kunnen zijn. Salah wordt boos en is daardoor aangehouden.")
        afgroet()
    elif vraag6 == "B":
        print("Het hele vliegveld wordt op alert gezet. Na een half uur is Awadh gevonden.")
        print("Na een grote schrik is Salah eindelijk weer een gelukkige man met zijn gezin opweg naar het aziel")
        vraag7()
    else:
        print("Verkeerde invoer, alleen Y of N")
        main()

def vraag7():
    print("====================================================")
    print("PART 2")
    print("====================================================")
    print("7. Eenmaal aangekomen in Ter Apel. Mona heeft geen gasfornuis meer, omdat alle nieuwkomers daar standaard maaltijden krijgen. Wat doet Mona?")
    print("A: Mona gaat opzoek naar andere gezinnen")
    print("B: Ze vraagt elke keer weer wat er in het eten zit van de dag")
    vraag7 = input("Kies A of B: ").upper()
    if vraag7 == "A":
        print("Mona vindt een ander Jemenitisch gezin in een gedeelte waar wel gekookt mag worden.")
        vraag8()
    elif vraag7 == "B":
        print("Hierdoor raakt Mona snel gestressed. dit doet haar denken aan de tijden toen ze een jaar lang in Saudi-Arabie moest overleven")
        vraag14()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag7()

def vraag8():
    print("====================================================")
    print("8. Eindelijk komt het gezin bij Salah in het azc in Rotterdam terecht. Nodigen jullie ook het andere gezin uit?")
    print("A: Ja")
    print("B: Nee")
    vraag8 = input("Kies A of B: ").upper()
    if vraag8 == "A":
        print("Salah heeft echte pure koffie gehaald, hij noemt het onovertroffen. Maar dat is niet zo volgens Mona. Het is niet haar smaak. ")
        vraag9()
    elif vraag8 == "B":
        print("Salah en zijn gezin zijn eindelijk weer bij elkaar.")
        vraag18()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag8()

def vraag9():
    print("====================================================")
    print("9. De grootste zorgen liggen nu achter hun. Wat was het omslagpunt van Mona?")
    print("A: Saswan zei dat ze een meisje hoorde schreeuwen: Mama, niemand heeft hier een stok in zijn hand!")
    print("B: Mona denkt terug aan haar verleden")
    vraag9 = input("Kies A of B: ").upper()
    if vraag9 == "A":
        print("Saswan weet dat ze een doorzetter is, die komt er wel! ")
        vraag10()
    elif vraag9 == "B":
        vraag14()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag9()

def vraag10():
    print("====================================================")
    print("10. Hoe noemt Salah Faleha?")
    print("A: Zus Faleha.")
    print("B: Faleha.")
    vraag10 = input("Kies A of B: ").upper()
    if vraag10 == "A":
        print("Zus, zo noem je een vriendin in het Arabisch. De relatie met iedereen is nog steeds sterk. Het word even wennen maar alles gaat goed.")
        vraag11()
    elif vraag10 == "B":
        vraag19()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag10()

def vraag11():
    print("====================================================")
    print("PART 3")
    print("====================================================")
    print("11. De omstandigheden zijn niet goed voor Awadh. Hij heeft niet genoeg te doen en te veel energie om eruit te gooien. Wat doet Salah hiertegen?")
    print("A: Voor nu nog niks. Eerst geld sparen en een beter leven proberen te lijden.")
    print("B: Salah brengt Awadh naar een trampoline park om zijn energie eruit te gooien.")
    vraag11 = input("Kies A of B: ").upper()
    if vraag11 == "A":
        print("De ouders moeten vaak nog met hem in de slaapkamer blijven, omdat hij altijd op het bed wilt springen.")
        vraag12()
    elif vraag11 == "B":
        vraag21()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag11()

def vraag12():
    print("====================================================")
    print("12. Geeft Salah Mona de schuld over de beperkingen van hun kind?")
    print("A: Nee.")
    print("B: Ja")
    vraag12 = input("Kies A of B: ").upper()
    if vraag12 == "A":
        print("Mona mag in haar handen knijpen met zo'n zorgname vader als Salah. Beide ouders zien Awadh als een cadeau van god, daar moeten ze voor zorgen.")
        vraag13()
    elif vraag12 == "B":
        print("Er groeien steeds meer ruzies in het gezin omdat Mona het niet leuk vindt dat Salah steeds ruzie maakt.")
        afgroet()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag12()

def vraag13():
    print("====================================================")
    print("13. Wat wilt Mona doen met haar toekomst?")
    print("A: Werken met kinderen met autisme.")
    print("B: Rusten. Naast hier en daar werken als vrijwilleger neemt Mona een stapje terug en blijft thuis.")
    vraag13 = input("Kies A of B: ").upper()
    if vraag13 == "A":
        print("En zo komt dit verhaal op z'n einde. Mona vind een baan waar ze kinderen met autisme kan helpen. Sawsan en Awadh gaan allebei weer naar school en krijgen nog een mooie toekomst voor hun. Salah is weer een gelukkige man.")
        afgroet()
    elif vraag13 == "B":
        print("Rusten. Naast hier en daar werken als vrijwilleger neemt Mona een stapje terug en blijft thuis.")
        afgroet()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag13()

def vraag14():
    print("====================================================")
    print("VERLEDEN")
    print("====================================================")
    print("Bijna een jaar moest Mona overleven zonder Salah.")
    print("====================================================")
    print("14. Wat deed Mona toen ze 15 was om Salah te ontmoeten?")
    print("A: Ze is als vijftienjarige gevlucht uit Irak.")
    print("B: Ze is zich gaan schuilen in Irak.")
    vraag14 = input("Kies A of B: ").upper()
    if vraag14 == "A":
        print("Mona moet een manier vinden om te vluchten.")
        vraag15()
    elif vraag14 == "B":
        print("Mona zal Salah nooit gevonden hebben. En niemand weet wat er met haar is gebeurt omdat ze nooit de kans heeft gekregen om te vluchten")
        afgroet()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag14()

def vraag15():
    print("====================================================")
    print("15. Hoe is Mona uit Irak gevlucht?")
    print("A: Ze gaat te voet proberen om uit het land te komen.")
    print("B: Ze vraagt aan een werkgever of hij haar uit het land kan smokkelen.")
    vraag15 = input("Kies A of B: ").upper()
    if vraag15 == "A":
        print("Mona komt niet meer verder. haar voeten doen pijn. Ze ziet objecten voor haar die er eigenlijk niet zijn. Ze neemt haar laatste adem langs de weg richting de grens van Irak.")
        afgroet()
    elif vraag15 == "B":
        print("Ze vraagt aan een werkgever of hij haar uit het land kan smokkelen.")
        vraag16()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag15()

def vraag16():
    print("====================================================")
    print("16. De werknemer weigert. Wat doet Mona?")
    print("A: Ze zegt dat ze voor hem zal werken terwijl hij haar uit het land brengt.")
    print("B: Ze sluipt stiekem in de vrachtwagen.")
    vraag16 = input("Kies A of B: ").upper()
    if vraag16 == "A":
        print("De man accepteert het offer. Mona komt het land uit en ontmoet Salah.")
        vraag17()
    elif vraag16 == "B":
        print("Mona word opgepakt op de grens. Niemand weet wat er met haar is gebeurt. Maar we weten wel dat ze nooit Salah heeft ontmoet.")
        afgroet()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag16()

def vraag17():
    print("====================================================")
    print("17. Komen mensen erachter dan Salah en Mona getrouwd zijn?")
    print("A: Nee")
    print("B: Ja.")
    vraag17 = input("Kies A of B: ").upper()
    if vraag17 == "A":
        print("De man accepteert het offer. Mona komt het land uit en ontmoet Salah.")
        vraag11()
    elif vraag17 == "B":
        print("Mona en Salah worden allebei vermoord omdat ze uit verschillende stammen komen. En het is niet toegestaan voor twee stammen om te trouwen.")
        afgroet()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag17()

def vraag18():
    print("====================================================")
    print("18. Koopt Salah echte pure bonen?")
    print("A: Ja.")
    print("B: Nee.")
    vraag18 = input("Kies A of B: ").upper()
    if vraag18 == "A":
        print("Salah besluit zijn geld weg te geven aan koffie bonen waar ze voor nu een lange tijd aan kunnen genieten, omdat er toch geen visite was.")
        vraag9()
    elif vraag18 == "B":
        print("Salah besluit zijn geld te bewaren omdat ze toch geen visite hebben.")
        vraag9()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag18()

def vraag19():
    print("====================================================")
    print("19. Waarom?")
    print("A: Omdat Salah Faleha niet een zus wilt noemen. Hij vindt dat disrespectvol naar zijn vrouw.")
    print("B: Omdat Faleha geen respect krijgt van Salah. Hij vind niet dat zij het verdient omdat zij niet netjes met hun omgaat.")
    vraag19 = input("Kies A of B: ").upper()
    if vraag19 == "A":
        vraag11()
    elif vraag19 == "B":
        vraag20()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag19()

def vraag20():
    print("====================================================")
    print("20. Gaan Salah en Faleha zitten om erover te praten?")
    print("A: Ja.")
    print("B: Nee.")
    vraag20 = input("Kies A of B: ").upper()
    if vraag20 == "A":
        print("Salah en Faleha vergeven elkaar.")
        vraag11()
    elif vraag20 == "B":
        print("Er groeien steeds meer ruzies in het gezin omdat Mona het niet leuk vindt dat Salah steeds ruzie maakt.")
        afgroet()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag20()

def vraag21():
    print("====================================================")
    print("21. Hoe eindigt het dagje uit met Awadh?")
    print("A: Goed. er zijn geen ongelukken gebeurt.")
    print("B: Fout, Awadh is van de trampoline gevallen en heeft zijn arm gebroken.")
    vraag20 = input("Kies A of B: ").upper()
    if vraag20 == "A":
        print("Goed. er zijn geen ongelukken gebeurt.")
        vraag12()
    elif vraag20 == "B":
        print("Naast het feit dat Awadh zijn arm heeft gebroken, is alles goed gekomen en brengt dit een einde van het verhaal over Salah.")
        afgroet()
    else:
        print("Verkeerde invoer, alleen Y of N")
        vraag20()



def afgroet():
    print("====================================================")
    print("Je hebt het einde gehaald! Ging het goed? ")

# Groet de speler
def afspelen(username):
    print('Hallo, %s.' % username)
    x = datetime.datetime.now()
    print("De datum en tijd is:")
    print(x)


# Zet alles op volgorde neer
def main():
    print("Hello you!, ik ben Raphael.")
    print("Wie ben jij?")
    username = input('Mijn naam is: ')
    afspelen(username)
    intro(username)
    vraag1()
    restart(username)


main()
