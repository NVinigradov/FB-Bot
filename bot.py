import random

desk = list(range(0, 9))
def If_Win(desks):
    win_pos = ((0,1,2),
               (3,4,5),
               (6,7,8),
               (0,3,6),
               (1,4,7),
               (2,5,8),
               (0,4,8),
               (2,4,6))
    for i in win_pos:
        if desks[i[0]] == desks[i[1]] == desks[i[2]]:
            return desks[i[0]]
    return 0

def FieldToDraw(board):
    print ("_" * 15)
    for i in range(3):
        yield ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        yield ("_" * 15)
def SetZero():
    valid = 0
    gamer_input = 0
    while not valid:
        gamer_input = random.randint(0,9)
        if gamer_input > 0 and gamer_input < 9 and (str(desk[gamer_input]) not in "XO"):
            desk[gamer_input] = "O"
            valid = True
        gamer_input = gamer_input + 1


def talkingWithPlayer(gamer_input):
    valid = 0
    while not valid:
        yield("Your turn")
        yield('\n')
        try:
            gamer_input = int(gamer_input)
        except:
            yield ("Invalid input...")
            continue
        if gamer_input >= 0 and gamer_input < 9:
            if (str(desk[gamer_input]) not in "XO"):
                desk[gamer_input] = "X"
                valid = True
            else:
                yield ("Busy...")
        else:
            yield ("Invalid input...")


