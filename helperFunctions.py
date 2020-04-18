import random

# black = 0
# white = 0

colors = [1, 2, 3, 4, 5, 6]

# generating a random code
def generateRandomBoard():
    code = list()
    for i in range(4):
        code.append(random.choice(colors))
    return code

# calculate the score of the guess
def scoreBoard(referenceBoard, guessBoard):
    rb = referenceBoard[:]
    gb = guessBoard[:]
    black = 0
    white = 0

    # calculate black
    for i in range(4):
        if rb[i] == gb[i]:
            black += 1
            rb[i] = 0
            gb[i] = 0

    # calculate white
    for i in range(4):
        if gb[i] != 0 and gb[i] in rb:
            white += 1
            index = rb.index(gb[i])
            rb[index] = 0
    return [black, white]