# Mit spil


def db(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# def ind(db):
#     inp = input('Skriv et tal fra 1-9')
#     if inp == 1:
#         ind = db[0]
#     elif inp == 2:
#         ind = db[1]
#     elif inp == 3:
#         ind = db[2]
#     elif inp == 4:
#         ind = db[3]
#     elif inp == 5:
#         ind = db[4]
#     elif inp == 6:
#         ind = db[5]
#     elif inp == 7:
#         ind = db[6]
#     elif inp == 8:
#         ind = db[7]
#     elif inp == 9:
#         ind = db[2]

#     return ind

def sæt_x_o(board,spiller,felt):
    board[felt] = spiller

def felt(board):
    feltet = ' '
    while feltet not in '0'or'1'or'2'or'3'or'4'or'5'or'6'or'7'or'8'or'9':
        print('Hvor vil du gerne sætte dit bogstav henne?: ')
        feltet = input()

    return int(feltet)


def vælg_x_o():
    player1 = ''
    while not (player1 == 'X' or player1 == 'O'):
        player1 = input('Spiller 1, vælg om du vil være X eller O: ')
        if player1 == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']


def hvemerførst():
    return 'player2'

x = True

while x == True:

    spillepladen = db([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']) 
    spiller1, spiller2 = vælg_x_o()
    tur = hvemerførst()

    print('Hvem starter? - Det gør ', tur)

    Erspilletigang = True

    while Erspilletigang == True:
        if tur == 'player2':
            ryk = felt(spillepladen)
            sæt_x_o(spillepladen,spiller1, ryk)
            print(spillepladen)


    Erspilletigang = False
    x = False