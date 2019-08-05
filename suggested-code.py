import random

def gen_data():
    '''
    This is a function to generate a sequence of numbers(1-100) with 1 number randomly missing
    '''
    numbers = list(range(1, 100))
    # The random package has a function called shuffle, like shuffling a deck of cards
    random.shuffle(numbers)
    numbers.pop()
    random.shuffle(numbers)
    return numbers

# print(gen_data())

def find_missing(sequence):
    '''
    solution below
    '''
    list = []
    for n in range(1,100):
        if n in sequence:
            pass
        else:
            print('The input sequence is:')
            print(sequence)
            print('The missing number is',n)

find_missing(gen_data())
