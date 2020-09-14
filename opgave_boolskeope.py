#Opgave 1.1

# def checker(tal):
#     if tal <= 4:
#         print('Tallet er mindre eller lig med 4')
#     else:
#         print('Tallet er ikke lig eller mindre end 4')

#     if tal > 47:
#         print('Tallet er større end 47')

#     else:
#         print('Tallet er mindre end 47')

#     if tal == 3:
#         print('Tallet er lig med 3')

#     else:
#         print('Tallet er ikke lige med 3')

#     if tal == 15:
#         print('Tallet er ikke lig med 15')

#     else:
#         print('Tallet er lig med 15')

#     if tal == 45 or 22:
#         print('Tallet er ikke lig med 45 eller 22')

#     else:
#         print('Tallet er lig med 45 eller 22')

#     if tal >= 4:
#         print('Taller er større eller lig med 4 og mindre end 15')

#     else:
#         print('Det modsatte-....') 


# checker(int(input('Skriv et tal: ')))


# resultat0 = 4
# resultat1 = 2
# resultat2 = 2 > 4
# resultat3 = resultat0 > resultat1
# resultat4 = resultat2 or resultat0 == resultat1
# print(resultat4)

# resultat0 = 2 > 2
# resultat1 = 44.4 == 44
# resultat2 = 2 > 3 or False or 4 <= 4
# resultat3 = 2*5 > 4*3 or 4 - 3 == 1 or resultat
# resultat = (resultat0 or resultat1) and (resultat2 or resultat3) and
# resultat1
# print(not resultat2)

#opgave 2.1

# def uligechecker(tal_fra_bruger):
#     if tal_fra_bruger % 2 == 0:
#         print('Tallet er lige')

#     else:
#         print('Tallet er ulige')
    
# uligechecker(int(input('Skriv et tal: ')))

# def over18(tal_fra_bruger):
#     if tal_fra_bruger >= 18:
#         print('Tilykke du er gammel nok!')
#     else:
#         print('Beklager du er ikke gemmelnok')

# over18(int(input('Skriv din alder: ')))

# def over18(tal_fra_bruger):
#     if tal_fra_bruger >= 18 and tal_fra_bruger < 120:
#         print('Tilykke du er gammel nok!')
#     elif tal_fra_bruger < 18 and tal_fra_bruger > 0:
#         print('Beklager du er ikke gemmelnok')
#     elif tal_fra_bruger <0:
#         print('Du lyver!')
#     elif tal_fra_bruger >120:
#         print('Aha, så du er verdens ældste person?')

# over18(int(input('Skriv din alder: ')))

# import math

# def menu_program(tal):
#     if tal == 1:
#         tal1 = int(input('Skriv det første tal :'))
#         tal2 = int(input('Skriv det andet tal: '))

#         print(tal1*tal2)

#     elif tal == 2:
#         radius = int(input('Skriv radius: '))
#         print(pow(radius,2)*math.pi) 

#     elif tal == 3:
#         tal_fra_bruger = int(input('Hvor gammel er du?: '))
#         if tal_fra_bruger >= 18:
#             print('Tilykke du er gammel nok!')
#         else:
#             print('Beklager du er ikke gemmel nok, du mangler: ', -tal_fra_bruger + 18, 'år')


# menu_program(int(input('Vælg imellem: // 1. multi // 2. arealet af en cirkel // 3. Tjek din alder')))