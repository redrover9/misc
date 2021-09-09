shift = input('Which shift will you finish working today? ')
if shift == 'none':
    off = input('What shift did you last work? ')
day = input('Which day of your shift or time off is it? ')

if shift == 'day':
    if day == 'one':
        print("Go to bed at 5 pm.")
    else:
        print("Go to bed at 9 pm.")
if shift == 'night':
    print('Go to bed at 8 am.')
if shift == 'afternoon':
    print('Go to bed at 6 am.')
if shift == 'none':
    if off == 'day':
        if day == 'one':
            print('Go to bed at 11 pm.')
        elif day == 'two':
            print('Go to bed at 1 am.')
        else:
            print('Go to bed at 3 am.')
    elif off == 'night':
        if day == 'one':
            print('Go to bed at 6 am.')
        elif day == 'two':
            print('Go to bed at 4 am.')
        elif day == 'three':
            print ('Go to bed at 2 am.')
        else:
            print('Go to bed at 12 am.')
    else:
        if day == 'one':
            print('Go to bed at 10 pm.')
        elif day == 'two':
            print('Go to bed at 8 pm.')
        else:
            print('Go to bed at 6 pm.')