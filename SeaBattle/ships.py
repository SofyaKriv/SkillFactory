# -- coding: utf-8 --

from random import randint

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Выстрел попадает за поле!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку!"

class BoardWrongShipException(BoardException):
    pass

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


class Ship:
    def __init__(self, length, x, y, rotation):
        self.length = length #длина корабля
        self.x = x #координата х носа корабля
        self.y = y #координата y носа корабля
        self.rotation = rotation #1 - вертикально, 0 - горизонтально
        self.lives = length #число жизней

    @property
    def dots(self):
        dots_all = []
        for i in range(self.length):
            dotx = self.x
            doty = self.y
            if self.rotation == 1:
                doty += i
            if self.rotation == 0:
                dotx += i
            dots_all.append(Dot(dotx, doty))
        return dots_all

    def shooten(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, hid=False):
        self.field = [["0", "0", "0", "0", "0", "0"],
                      ["0", "0", "0", "0", "0", "0"],
                      ["0", "0", "0", "0", "0", "0"],
                      ["0", "0", "0", "0", "0", "0"],
                      ["0", "0", "0", "0", "0", "0"],
                      ["0", "0", "0", "0", "0", "0"]]
        self.ships = []
        self.hid = hid
        self.alive = []
        self.busy = []
        self.count = 0

    def __str__(self):
        res = ""
        res += "  | 0 | 1 | 2 | 3 | 4 | 5 |"
        for i, row in enumerate(self.field):
            res += f"\n{i} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "0").replace(".", "0")
        return res

    def out(self, dot):
        if (0 <= dot.x < 6) and (0 <= dot.y < 6):
            return False
        else:
            return True

    def shot(self, dot):
        if self.out(dot):
            return BoardOutException()

        if dot in self.busy:
            return BoardUsedException()

        for ship in self.ships:
            if dot in ship.dots:
                ship.lives -= 1
                self.field[dot.x][dot.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Вы уничтожили корабль!")
                    return False
                else:
                    print("Вы попали в корабль!")
                    return True
            else:
                self.field[dot.x][dot.y] = "."
                print("Выстрел мимо!")
                return False
        self.busy.append(dot)

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.out(dot) or dot in self.busy:
                raise BoardWrongShipException()
            self.field[dot.x][dot.y] = "■"
            self.busy.append(dot)
        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        pos = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
        for dot in ship.dots:
            for i, j in pos:
                cont_dot = Dot(dot.x + i, dot.y + j)
                if not self.out(cont_dot) and cont_dot not in self.busy:
                    if verb:
                        self.field[cont_dot.x][cont_dot.y] = "."
                    self.busy.append(cont_dot)

    def begin(self):
        self.busy = []


class Player:
    def __init__(self, my_board, enemy_board):
        self.my_board = my_board
        self.enemy_board = enemy_board

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy_board.shot(target)
                return repeat
            except:
                print(BoardException())


class AI(Player):
    def ask(self):
        dot = Dot(randint(0, 5), randint(0, 5))
        print(f"Компьютер пульнул сюда: {dot.x, dot.y}")
        return dot


class User(Player):
    def ask(self):
        while True:
            coord = input("Ваш ход: ").split()
            if len(coord) != 2:
                print("Введите 2 координаты точки!")
                continue
            x, y = coord
            if not x.isdigit() or not y.isdigit():
                print("Нужны числа!")
                continue
            if int(x) < 0 or int(x) > 5 or int(y) < 0 or int(y) > 5:
                print(BoardOutException())
                continue
            return Dot(int(x), int(y))


class Game:
    def __init__(self):
        ai_board = self.random_board()
        user_board = self.random_board()
        self.ai = AI(ai_board, user_board)
        self.user = User(user_board, ai_board)

        ai_board.hid = True

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        ship_len = [3, 2, 2, 1, 1, 1, 1]
        board = Board()
        t = 0
        for l in ship_len:
            while True:
                ship = Ship(l, Dot(randint(0, 6), randint(0, 6)).x, Dot(randint(0, 6), randint(0, 6)).y, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
                t += 1
                if t > 10000:
                    return None
        board.begin()
        return board

    def greet(self):
        print("Приветствуем в игре \"Морской бой\"")
        print("Для того, чтобы сделать ход, введите две координаты: x и y")

    def loop(self):
        num = 0
        while True:
            print("Доска игрока:")
            print(self.user.my_board)
            print("Доска компьютера:")
            print(self.ai.my_board)
            if num % 2 == 0:
                print("Ходит игрок!")
                repeat = self.user.move()
            else:
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1
            if self.ai.my_board.count == 7:
                print("Игрок выиграл!")
                break
            if self.user.my_board.count == 7:
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()

g = Game()
g.start()



