
s = 'rzsa'

def funnyString(s):
    ascii_list = [ord(x) for x in s ]
    subtracted_list = []

    for i in range(len(ascii_list)-1):
        subtracted_nums = ascii_list[i]-ascii_list[i+1]
        subtracted_list.append(abs(subtracted_nums))
    if subtracted_list == subtracted_list[::-1]:
        print ('Funny')
    elif subtracted_list != subtracted_list[::-1]:
        return ('Not Funny')

funnyString(s)