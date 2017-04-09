#  10 denotes a Straight Flush
#   9 denotes a four of a kind
#   8 denotes a fullhouse

VALS = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def vald(a):
    return VALS[a]


def isSF(h):  # OK
    r = [-1, -1]
    if h[0] == h[1] == h[2] == h[3] == h[4]:
        r = [10, h[4][0]]
    return r


def isFK(h):  # OK
    sorted(vald, key=vald)
    r = [-1, -1]
    if h[0][0] == h[1][0] == h[2][0] == h[3][0]:
        r = [9, h[3][0]]
    elif [1][0] == h[2][0] == h[3][0] == h[4][0]:
        r = [9, h[3][0]]
    return r


def isFH(h):
    sorted(vald, key=vald)
    r = [-1, -1]
    if (h[0][0] == h[1][0] == h[2][0]) and (h[3][0] == h[4][0]):
        r = [8, h[2][0]]
    elif (h[1][0] == h[2][0]) and (h[3][0] == h[4][0] == h[5][0]):
        r = [8, h[3][0]]
    return r


def isFL(h):
    sorted(vald, key=vald)
    r = [-1, -1]
    if h[0][1] == h[1][1] == h[2][1] == h[3][1] == h[4][1]:
        r = [7, h[4][1]]
    return r


def isST(h):
    sorted(vald, key=vald)
    r = [-1, -1]
    bf1 = VALS[h[1][0]] == (VALS[h[0][0]] + 1)
    bf2 = VALS[h[2][0]] == (VALS[h[1][0]] + 1)
    bf3 = VALS[h[3][0]] == (VALS[h[2][0]] + 1)
    bf4 = VALS[h[4][0]] == (VALS[h[3][0]] + 1)
    if bf1 and bf2 and bf3 and bf4:
        r = [6, h[4][0]]

    return [-1, -1]


def isTOK(h):
    sorted(vald, key=vald)
    r = [-1, -1]
    bf1 = (h[0][0] == h[1][0] == h[2][0])
    bf2 = (h[1][0] == h[2][0] == h[3][0])
    bf3 = (h[2][0] == h[3][0] == h[4][0])
    if bf1 or bf2 or bf3:
        r = [5, h[2][0]]


def is2P(h):
    sorted(vald, key=vald)
    r = [-1, -1]
    if h[0][0] == h[1][0] and h[1][0] == h[2][0]:
        r = [4, h[1][0]]
    if h[2][0] == h[3][0] and h[3][0] == h[4][0]:
        r = [4, max(r[1], h[3][0])]
    return r


def isP(h):
    sorted(vald, key=vald)
    r = [-1, -1]
    if h[0][0] == h[1][0] or h[1][0] == h[2][0]:
        r = [3, h[1][0]]
    elif h[2][0] == h[3][0] or h[3][0] == h[4][0]:
        r = [3, h[3][0]]
    return r


def isHC(h):
    sorted(vald, key=vald)
    bf1 = (h[0][0] == h[1][0] == h[2][0])
    bf2 = (h[1][0] == h[2][0] == h[3][0])
    bf3 = (h[2][0] == h[3][0] == h[4][0])
    return bf1 or bf2 or bf3
# NO NEED TO TEST FOR HIGH CARD

while True:
    cards = input().split(' ')
    if len(cards) == 0:
        break

    p1h = [cards[0], cards[1], cards[2], cards[3], cards[4]]
    p2h = [cards[5], cards[6], cards[7], cards[8], cards[9]]

    p1r = [-1, -1]
    p2r = [-1, -1]

    i = 10
    win = [0, 0]
    while (p1r == [-1, -1]) or (p2r == [-1, -1]):
        if i == 10:
            if ifSF(p1h):
                p1r = [10, cards[0][0]]
                win[0] = 1
            if ifSF(p2h):
                p1r = [10, cards[0][0]]
                win[1] = 1
        elif i == 9:
            if isFK(p1h):
                p1r = [10, cards[3][0]]
                win[0] = 1
            if isFK(p2h):
                p1r = [10, cards[3][0]]
                win[1] = 1
        elif i == 8:
            if isFH(p1h):
                p1r = [10, cards[3][0]]
                win[0] = 1
            if isFH(p2h):
                p1r = [10, cards[3][0]]
                win[1] = 1
        elif i == 7:
            if isFH(p1h):
                p1r = [10, cards[3][0]]
                win[0] = 1
            if isFH(p2h):
                p1r = [10, cards[3][0]]
                win[1] = 1
