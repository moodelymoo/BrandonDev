def fizzBuzzVerbose():
    for i in range(101):
        if i == 0:
            continue
        elif i % 15 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)


def fizzBuzzOneLine():
    # in terms of readability this is not that easy to follow, but this is how to do fizzbuzz int the fewest
    # characters that i can think of
    for i in range(1, 101): print("Fizz" * (i % 3 < 1) + (i % 5 < 1) * "Buzz" or i)


def fizzBuzzVerboseAsString():
    ls = list()
    for i in range(101):
        if i == 0:
            continue
        elif i % 15 == 0:
            ls.append('FizzBuzz')
        elif i % 5 == 0:
            ls.append('Buzz')
        elif i % 3 == 0:
            ls.append('Fizz')
        else:
            ls.append(i)
    return ls

