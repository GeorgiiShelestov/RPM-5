from random import randint
import os

import copy
import keyboard as kb

VOID = '  '
ALL_TOWERS_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
towers_rings = {}
rings = []


def input_towers():
    towers_num = int(input('Введите количество башен: '))
    if towers_num > 10 or towers_num < 3:
        print('Количество башен от 3 до 10')
        return input_towers()
    else:
        for i in range(towers_num):
            towers_rings[ALL_TOWERS_NAMES[i]] = []
        return input_rings(towers_num)


def input_rings(towers_num):
    rings_num = int(input('Введите количество блинов: '))
    if rings_num > 20 or rings_num < 0:
        print('Количество блинов от 3 до 20')
        return input_rings(towers_num)
    elif rings_num < 10:
        for i in range(rings_num):
            ring = '\033[{}m{}'.format(i + 31, '█') * (i + 1)
            ring += ' ' * (rings_num - (i - (rings_num - 4)))
            rings.append(ring)
        rings.reverse()
        return input_start_tower(towers_num, rings_num)
    else:
        for i in range(9):
            ring = '\033[{}m{}'.format(i + 31, '█') * (i + 1)
            ring += ' ' * (rings_num - (i - (rings_num - 4)))
            rings.append(ring)
        for i in range(rings_num - 9):
            ring = '\033[{}m{}'.format(i + 31, '█') * (i + 10)
            ring += ' ' * (rings_num - (i - (rings_num - 4)))
            rings.append(ring)
        rings.reverse()
        return input_start_tower(towers_num, rings_num)


def input_start_tower(towers_num, rings_num):
    start_tower = int(input('Введите номер начальной башни: '))
    if start_tower > towers_num:
        print('Ваше количество башен - {}'.format(towers_num))
        return input_start_tower(towers_num, rings_num)
    else:
        towers_rings[ALL_TOWERS_NAMES[start_tower - 1]] = rings
        start_tower_letter = ALL_TOWERS_NAMES[start_tower - 1]
        return input_end_tower(towers_num, rings_num, start_tower, start_tower_letter)


def input_end_tower(towers_num, rings_num, start_tower, start_tower_letter):
    rings_num_copy = rings_num
    end_tower = int(input('Введите номер конечной башни: '))
    if end_tower > towers_num:
        print('Ваше количество башен - {}'.format(towers_num))
        return input_end_tower(towers_num, rings_num, start_tower, start_tower_letter)
    else:
        end_tower_letter = ALL_TOWERS_NAMES[end_tower - 1]
        NECESSARY_TOWERS = ALL_TOWERS_NAMES[:towers_num]
        del_start_poz = NECESSARY_TOWERS[start_tower - 1]
        del_end_poz = NECESSARY_TOWERS[end_tower - 1]
        NECESSARY_TOWERS.pop(NECESSARY_TOWERS.index(del_start_poz))
        NECESSARY_TOWERS.pop(NECESSARY_TOWERS.index(del_end_poz))
        move(copy.deepcopy(towers_rings), NECESSARY_TOWERS, rings_num_copy)
        return tower_of_hanoi(
            rings_num, start_tower_letter, NECESSARY_TOWERS[randint(0,len(NECESSARY_TOWERS))-1],
            end_tower_letter, NECESSARY_TOWERS, rings_num_copy)


def tower_of_hanoi(numbers, start, auxiliary, end, Towers, rings_num_copy):
    if numbers == 1:
        towers_rings[end].append(towers_rings[start].pop())
        move(copy.deepcopy(towers_rings), Towers, rings_num_copy)
        return
    tower_of_hanoi(numbers - 1, start, end, auxiliary, Towers, rings_num_copy)
    towers_rings[end].append(towers_rings[start].pop())
    move(copy.deepcopy(towers_rings), Towers, rings_num_copy)
    tower_of_hanoi(numbers - 1, auxiliary, start, end, Towers, rings_num_copy)
    return


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def move(towers_rings, Towers, rings_num):
    while True:
        key = kb.read_key()
        if key in ['enter']:
            break
    while True:
        key = kb.read_key()
        if key in ['enter']:
            break
    all = ''
    for i in range(rings_num):
        for k in towers_rings:
            if len(towers_rings[k]) != rings_num - i:
                all += VOID*(rings_num-1)
            else:
                try:
                    all += ' {}'.format(str(towers_rings[k].pop()))
                except:
                    pass
        print(all)
        all = ''
    void_between_towers = '_'
    void_between_towers += ' ' * rings_num
    void_between_towers += ' ' * (rings_num-3)
    print('\033[{}m {}'.format('30', void_between_towers * (len(Towers) + 2)))


if __name__ == '__main__':
    input_towers()