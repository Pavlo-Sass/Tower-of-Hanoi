import time

def create_tower(n):
    return [list(reversed([i for i in range(1, n+1)])), [], []]

def check_win(n):
    return [[], list(reversed([i for i in range(1, n+1)])), []]

def turn(towers, combination):
    last_value = ['*', '*']
    for i in range(2):
        if len(towers[combination[i]]) == 0:
            last_value[i] = 999
        else:
            last_value[i] = towers[combination[i]][-1]

    if last_value[0] < last_value[1]:
        towers[combination[1]].append(towers[combination[0]].pop())
    else:
        towers[combination[0]].append(towers[combination[1]].pop())
    return towers

def output(n, towers):
    down = "\n" * 20
    print(down)
    for i in reversed(range(n)):
        if len(towers[0]) <= i:
            first = "|"
        else:
            first = str(towers[0][i]) * towers[0][i]
        if len(towers[1]) <= i:
            second = "|"
        else:
            second = str(towers[1][i]) * towers[1][i]
        if len(towers[2]) <= i:
            third = "|"
        else:
            third = str(towers[2][i]) * towers[2][i]
        print('{: ^10}{: ^10}{: ^10}'.format(first, second, third))

def main():
    n = greating()
    towers = create_tower(n)
    output(n, towers)
    win = check_win(n)
    if n % 2 == 1:
        combinations = (0, 1), (0, 2), (1, 2)
    else:
        combinations = (0, 2), (0, 1), (1, 2)
    while True:
        for combination in combinations:
            time.sleep(0.5)
            towers = turn(towers, combination)
            output(n, towers)
            if towers == win:
                time.sleep(3)
                youwin()
                return

def greating():
    start_text = ''' _____  _   _  _____   ______  _____ ______   ___  ___  ___ _____ ______  _   __  ___  
|_   _|| | | ||  ___|  | ___ \|_   _|| ___ \ / _ \ |  \/  ||_   _||  _  \| | / / / _ \ 
  | |  | |_| || |__    | |_/ /  | |  | |_/ // /_\ \| .  . |  | |  | | | || |/ / / /_\ \\
  | |  |  _  ||  __|   |  __/   | |  |    / |  _  || |\/| |  | |  | | | ||    \ |  _  |
  | |  | | | || |___   | |     _| |_ | |\ \ | | | || |  | | _| |_ | |/ / | |\  \| | | |
  \_/  \_| |_/\____/   \_|     \___/ \_| \_|\_| |_/\_|  |_/ \___/ |___/  \_| \_/\_| |_/'''
    print(start_text)
    print('___________________________________________________________________by PAVLO SASS')
    time.sleep(3)
    how_many_text = '''
_   _                                                       _             _      _         _          ___  
| | | |                                                     | |           | |    | |       | |        |__ \ 
| |_| |  ___  __      __   _ __ ___    __ _  _ __   _   _   | |__   _   _ | |__  | | _   _ | | __ ___    ) |
|  _  | / _ \ \ \ /\ / /  | '_ ` _ \  / _` || '_ \ | | | |  | '_ \ | | | || '_ \ | || | | || |/ // __|  / / 
| | | || (_) | \ V  V /   | | | | | || (_| || | | || |_| |  | |_) || |_| || |_) || || |_| ||   < \__ \ |_|  
\_| |_/ \___/   \_/\_/    |_| |_| |_| \__,_||_| |_| \__, |  |_.__/  \__,_||_.__/ |_| \__, ||_|\_\|___/ (_)  
                                                     __/ |                            __/ |                 
                                                    |___/                            |___/                  
'''
    print(how_many_text)
    while True:
        number_str = input('Enter numbers of BUBLYKS (from 3 to 9)')
        if number_str.isdigit():
            number = int(number_str)
            if 3 <= number <= 9:
                break
    loading_text = """
 _                        _  _               
| |                      | |(_)              
| |      ___    __ _   __| | _  _ __    __ _ 
| |     / _ \  / _` | / _` || || '_ \  / _` |
| |____| (_) || (_| || (_| || || | | || (_| |
\_____/ \___/  \__,_| \__,_||_||_| |_| \__, |
                                        __/ |
                                       |___/ 
    """
    print(loading_text)
    for i in range(40):
        print("#", end='')
        time.sleep(0.1)
    return number

def youwin():
    win_text = """
    ______  _____  _____ ______   ___   _____  _   _  _____  _   _  _____ 
    | ___ \|  _  ||_   _|| ___ \ / _ \ /  __ \| | | ||  ___|| \ | ||  _  |
    | |_/ /| | | |  | |  | |_/ // /_\ \| /  \/| |_| || |__  |  \| || | | |
    |  __/ | | | |  | |  |    / |  _  || |    |  _  ||  __| | . ` || | | |
    | |    \ \_/ /  | |  | |\ \ | | | || \__/\| | | || |___ | |\  |\ \_/ /
    \_|     \___/   \_/  \_| \_|\_| |_/ \____/\_| |_/\____/ \_| \_/ \___/ """
    print(win_text)
k = 9
main()
