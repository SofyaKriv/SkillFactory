# -- coding: utf-8 --

list_of_var = ['0', 'X', 'x', 'х', 'Х', 'O', 'o']

def check_func(x):
    if x not in list_of_var:
        return False
    else:
        return True

print("Выберите, за кого будете играть: '0' или 'X'?")
player1 = input("Игрок 1: ")
if check_func(player1):
    print("Принято")
else:
    while not check_func(player1):
        print("Вы не можете использовать значение " + player1 + " для игры. Выберите, пожалуйста, 0 или Х")
        player1 = input("Игрок 1: ")
        if check_func(player1):
            print("Принято")
if player1 == '0' or player1 == 'O' or player1 == 'o':
    player2 = 'X'
    print("Игрок 2, Вы будете играть за " + player2)
else:
    player2 = '0'
    print("Игрок 2, Вы будете играть за " + player2)
print("Ну, что ж, приступим!")

play = [['', '', ''], ['', '', ''], ['', '', '']]

digit_list = ['0', '1', '2']

def get_cord():
    st = input()
    x0, y0 = st.split(' ')[0], st.split(' ')[1]
    if not x0 in digit_list or not y0 in digit_list:
        print("Значения выходят за пределы поля")
        get_cord()
    else:
        x, y = int(st.split(' ')[0]), int(st.split(' ')[1])
    return x, y

def draw():
    print("   | 0 | 1 | 2 |")
    print("----------------")
    print(" 0 | " + play[0][0] + " | " + play[0][1] + " | " + play[0][2] + " |")
    print("-------------")
    print(" 1 | " + play[1][0] + " | " + play[1][1] + " | " + play[1][2] + " |")
    print("-------------")
    print(" 2 | " + play[2][0] + " | " + play[2][1] + " | " + play[2][2] + " |")
    print("-------------")

win_scene = (((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)), ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)))

count = 0

def check_win():
    for line in win_scene:
        scene_set = []
        for s in line:
            scene_set.append(play[s[0]][s[1]])
        if scene_set == ['X', 'X', 'X'] or scene_set == ['x', 'x', 'x'] or scene_set == ['х', 'х', 'х'] or scene_set == ['Х', 'Х', 'Х']:
            print("Выиграл X")
            return True
        elif scene_set == ['0', '0', '0'] or scene_set == ['o', 'o', 'o'] or scene_set == ['O', 'O', 'O'] or scene_set == ['О', 'О', 'О'] or scene_set == ['о', 'о', 'о']:
            print("Выиграл 0")
            return True
    return False

def check_step(x, y):
    if play[x][y] == '':
        if p == 1:
            play[x][y] = player1
        else:
            play[x][y] = player2
        return True
    else:
        print("Здесь уже стоит значение! Введите снова")
        return False

while True:
    print("Введите две координаты позиции хода")
    count += 1
    p = count % 2
    if p == 1:
        print("Ход первого игрока")
    else:
        print("Ход второго игрока")
    x, y = get_cord()
    while not check_step(x, y):
        x, y = get_cord()
        if check_step(x, y):
            break
    draw()
    if check_win():
        break
    if count == 9:
        print("Ничья")
        break



