from time import sleep


def generate_map(x, y) -> list:
    res = []
    x, y = int(x), int(y)

    for i in range(y):
        section = []
        for j in range(x):
            section.append(' ')
        res.append(section)
    
    return res

def show_map(map, pos:list, margin:bool=True):
    x = len(map[0])
    y = len(map)
    sym = map[pos[1]][pos[0]]
    map[pos[1]][pos[0]] = '*'

    if margin:
        res = ('--' * x) + '-\n'

        for i in range(y):
            for j in range(x):
                res += f'|{map[i][j]}'
            res += '|\n'
            res += ('--' * x) + '-\n'
    else:
        res = ''    

        for i in range(y):
            for j in range(x):
                if m[i][j] == ' ':
                    res += '_'
                else:
                    res += f'{map[i][j]}'
            res += '\n'

    print(res)

    map[pos[1]][pos[0]] = sym

def move(pos, x, y, comadnd) -> list:
    if comadnd == 's':
        if pos[1] + 1 > y - 1:         
            print('end of list.')
        else:
            pos[1] += 1
    elif comadnd == 'a':
        if pos[0] - 1 < 0:
            print('end of list.')
        else:
            pos[0] -= 1
    elif comadnd == 'w':
        if pos[1] - 1 < 0:
            print('end of list.')
        else:
            pos[1] -= 1
    elif comadnd == 'd':
        if pos[0] + 1 > x - 1:
            print('end of list.')
        else:
            pos[0] += 1
    
    return pos

def change_xy() -> int:
    x = int(input('wide: '))
    y = int(input('height: '))

    return x,y

def save(map):
    res = ''

    filename = input('input file name(CANC for cancel): ')
    if filename != 'CANC':
        x = len(map[0])
        y = len(map)
        with open(f'{filename}.txt', 'w+') as file:
            for i in range(y):
                podres = ''
                for j in range(x):
                    podres += map[i][j]
                podres += '\n'
                res += podres
            
            file.write(res)
    print('file saved')

def help():
    commands = [
        'COMMAND LIST:',
        'shm - show art'
        'help - print this window',
        'margin - on/off margin',
        'wasd - move pen',
        'pchar - show current print char',
        'setpchar - set print char' 
        'p - print case in print symbol',
        'c - clear case',
        'save - save art to txt file',
        'exit - close program'
        ]
    
    for command in commands:
        print(command)

# init
nrdy = True
while nrdy:
    try:
        x,y = change_xy()
        nrdy = False
    except BaseException:
        print('please type numbers only')

map = generate_map(x, y)
pos = [0, 0]
pchar = '0'

margin = True
run = True

print('type help for command list')
show_map(map, pos, margin)

while run:

    tasks = input('>')
    tasks = tasks.split(' ')

    for task in tasks:
        if task == 'help':
            help()
        elif task == 'exit':
            run = False
        elif task == 'margin':
            margin = not margin
            if margin:
                print('margin on')
            else:
                print('margin off')
        elif task == ('shm'):
            m = map
            show_map(m, pos, margin)
        elif task == 'w' or task == 'a' or task == 's' or task == 'd':
            move(pos, x, y, task)
        elif task == 'c':
            map[pos[1]][pos[0]] = ' '
        elif task == 'p':
            map[pos[1]][pos[0]] = pchar
        elif task == 'pchar':
            print(pchar)
        elif task == 'setpchar':
            ask = input('input pchar: ')
            if ask != '' and len(ask) == 1: pchar = str(ask)
        elif task == 'save':
            save(map)

        sleep(0.15)