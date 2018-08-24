'''Tic Tac Toe game'''
def check(seti):
    '''checking values and elements in set'''
    if 'x' in seti:
        return 'x'
    return 'o'
def playgame(game):
    '''gamerules'''
    cond1 = set()
    cond2 = set()
    cond3 = set()
    cond4 = set()
    cond5 = set()
    len1 = len(game)
    for i in range(len1):
        for j in range(len(game[i])):
            if i == j:
                cond1.add(game[i][j])
            if i + j == (len1 - 1):
                cond2.add(game[i][j])
            cond = set(game[i])
            if len(cond) == 1:
                if 'x' in cond:
                    return 'x'
                return 'o'
            if j == 0:
                cond3.add(game[i][j])
            if j == 1:
                cond4.add(game[i][j])
            if j == 2:
                cond5.add(game[i][j])
    if len(cond1) == 1:
        return check(cond1)
    if len(cond2) == 1:
        return check(cond2)
    if len(cond3) == 1:
        return check(cond3)
    if len(cond4) == 1:
        return check(cond4)
    if len(cond5) == 1:
        return check(cond5)
    return "Match drawn"

def validcheck(game):
    '''Validating the players'''
    x = 'x'
    o = 'o'
    cntofx = 0
    cntofo = 0
    cntofdot = 0
    for index in game:
        if x in index:
            cntofx += index.count(x)
        if o in index:
            cntofo += index.count(o)
        if '.' in index:
            cntofdot += index.count('.')
        if len(index) != 3:
            return "invalid game"
    if cntofx + cntofo + cntofdot != 9:
        return "invalid input"
    if abs(cntofx - cntofo) != 1:
        return "invalid game"
    return playgame(game)


def main():
    '''Main function'''
    row = []
    for _ in range(3):
        column = input()
        column = list(map(str, column.split(' ')))
        row.append(column)
    row = validcheck(row)
    print(row)

if __name__ == '__main__':
    main()
