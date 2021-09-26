print('How many cats do you habe?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('this is a lot of cats.')
    else:
        print('this is not that many cats.')
except ValueError:
    print('You did not enter a number')