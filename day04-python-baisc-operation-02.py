# https://ithelp.ithome.com.tw/articles/10193001

# count = 0
# while count < 5:
#     print(count)
#     count = count +1

# count = 0
# if count < 5:
#     print(count)
#     count = count +1

# def my_first_func():
#     print('Call this function!')
# my_first_func()

"""
guess number
"""
import random
scrnum = random.randint(1, 10)
print('guess a number between 1 and 10')
for guess_num in range(1,7):
    print('guess number:')
    guess = int(input())
    print('==========')
    if guess < guess_num:
        print('too low')
    elif guess > guess_num:
        print('too high')
    else:
        print('Guess right！')
        break