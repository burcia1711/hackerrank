def print_formatted(number):
    pad = number.bit_length()
    for i in range(1,number+1):
        print(format(i,'d').rjust(pad),
            format(i,'o').rjust(pad),
            format(i,'X').rjust(pad),
            format(i,'b').rjust(pad))