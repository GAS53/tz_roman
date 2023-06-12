from const import PERMIT_VALUES

def check_chars(val):
    '''проверка что есть только разрешенные цифры'''
    li_chars = list(val)
    for ch in li_chars:
        if ch not in PERMIT_VALUES.keys():
            raise ValueError(f'Неверно задано число - {ch}')
    return li_chars

    
def find_subrtakt(digits):
    '''проверка на случаи с субстрактивной записью
    проверка что все числа стоят по возрастанию иначе - значение'''
    new = 0
    pre_digit = None
    for i in digits:
        if pre_digit != None:
            if pre_digit >= i:
                new += pre_digit
            else:
                new -= pre_digit

        pre_digit = i
    new += pre_digit
    return new









if __name__ == '__main__':
    chars = check_chars('MCCXXXIV')
    li = [PERMIT_VALUES.get(i) for i in chars]
    print(find_subrtakt(li))