'''Tic Tac Toe game'''
def check(seti):
    '''checking values and elements in set'''
    if 'x' in seti:
        return 'x'
    return 'o'
def playgame(game):
    '''gamerules'''
    set1 = set()
    set2 = set()
    set3 = set()
    set4 = set()
    set5 = set()
    len1 = len(game)
    for i in range(len1):
        for j in range(len(game[i])):
            if i == j:
                set1.add(game[i][j])
            if i + j == (len1 - 1):
                set2.add(game[i][j])
            sett = set(game[i])
            if len(sett) == 1:
                if 'x' in sett:
                    return 'x'
                return 'o'
            if j == 0:
                set3.add(game[i][j])
            if j == 1:
                set4.add(game[i][j])
            if j == 2:
                set5.add(game[i][j])
    if len(set1) == 1:
        return check(set1)
    if len(set2) == 1:
        return check(set2)
    if len(set3) == 1:
        return check(set3)
    if len(set4) == 1:
        return check(set4)
    if len(set5) == 1:
        return check(set5)
    return "draw"

def validcheck(game):
    '''Validating the players'''
    x_element = 'x'
    o_element = 'o'
    countofx = 0
    countofo = 0
    countofdot = 0
    for index in game:
        if len(index) != 3:
            return "invalid game"
        if x_element in index:
            countofx += index.count(x_element)
        if o_element in index:
            countofo += index.count(o_element)
        if '.' in index:
            countofdot += index.count('.')
    if countofx + countofo + countofdot != 9:
        return "invalid input"
    if abs(countofx - countofo) != 1:
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
