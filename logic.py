# [Схема оценки]
# Точки для учета:
# Элементы матрицы должны быть равными, но не идентичными
# 1 балл за создание правильной матрицы
def new_game(n):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    matrix = add_two(matrix)
    matrix = add_two(matrix)
    return matrix



# [Схема оценки]
# Точки для учета:
# Необходимо убедиться, что элемент создан на пустой клетке
# 1 балл за создание правильного цикла

def add_two(mat):
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    while mat[a][b] != 0:
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    mat[a][b] = 2
    return mat

# [Схема оценки]
# Точки для учета:
# Элементы матрицы должны быть равными, но не идентичными
# 0 баллов за совершенно неверное решение
# 1 балл за правильное выполнение только одного условия
# 2 балла за правильную проверку двух из трех условий
# 3 балла за корректную проверку

def game_state(mat):
    # проверка на ячейку победы
    for i in range(len(mat)):
        for j in range(len(mat[0]):
            if mat[i][j] == 2048:
                return 'победа'
    # проверка на наличие нулевых записей
    for i in range(len(mat)):
        for j in range(len(mat[0]):
            if mat[i][j] == 0:
                return 'не окончена'
    # проверка на смежные ячейки с одинаковыми значениями
    for i in range(len(mat)-1):
        # специально уменьшили для проверки строки справа и снизу
        # более изящное использование исключений, но скорее всего это их решение
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'не окончена'
    for k in range(len(mat)-1):  # проверка левой / правой записей на последней строке
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'не окончена'
    for j in range(len(mat)-1):  # проверка записей вверх / вниз в последнем столбце
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'не окончена'
    return 'поражение'

###########
# Task 2a #
###########

# [Схема оценки]
# Точки для учета:
# 0 баллов за совершенно неверное решение
# 1 балл за решение, которое показывает общее понимание
# 2 балла за правильное решение, которое работает для всех размеров матриц

def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new


# [Схема оценки]
# Точки для учета:
# 0 баллов за совершенно неверное решение
# 1 балл за решение, которое показывает общее понимание
# 2 балла за правильное решение, которое работает для всех размеров матриц

def transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new

# [Схема оценки]
# Точки для учета:
# Способ перемещения - сжатие -> объединение -> сжатие снова
# В основном, если они могут решить одну из сторон и правильно использовать
# транспонирование и реверс, они должны быть способны решить всю задачу, просто развернув матрицу
# Нет идей, как оценивать это в данный момент. У меня установлено на 8 баллов (что дает примерно
# по 2 балла за вверх/вниз/влево/вправо?), но если вы получите одну правильную, скорее всего получите все остальные.
# Проверьте команду вниз. Реверс/транспонирование, если они указаны неправильно, дадут неправильный результат.


def cover_up(mat):
    new = []
    for j in range(c.GRID_LEN):
        partial_new = []
        for i in range(c.GRID_LEN):
            partial_new.append(0)
        new.append(partial_new)
    done = False
    for i in range(c.GRID_LEN):
        count = 0
        for j in range(c.GRID_LEN):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done

def merge(mat, done):
    for i in range(c.GRID_LEN):
        for j in range(c.GRID_LEN-1):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True
    return mat, done

def up(game):
    print("up")
    # вернуть матрицу после сдвига вверх
    game = transpose(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(game)
    return game, done

def down(game):
    print("down")
    # вернуть матрицу после сдвига вниз
    game = reverse(transpose(game))
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(reverse(game))
    return game, done

def left(game):
    print("left")
    ## вернуть матрицу после сдвига влево
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    return game, done

def right(game):
    print("right")
    # вернуть матрицу после сдвига вправо
    game = reverse(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = reverse(game)
    return game, done