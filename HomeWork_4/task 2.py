

def displays_even_number(number_one, number_two):
    '''Функция принимает два числа и отображает чётные числа между ними'''
    for even in range(number_one, number_two):
        if even % 2 == 0:
            print(even)



displays_even_number(3, 23)



