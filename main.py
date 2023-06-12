from utils import check_chars, find_subrtakt
from const import PERMIT_VALUES

def run(source):
    '''Основная рабочая функция'''
    chars = check_chars(source)
    digits = [PERMIT_VALUES.get(i) for i in chars]
    sub = find_subrtakt(digits)
    return sub

    

if __name__ == '__main__':
    print(run('CMXCIX'))