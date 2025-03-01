'''
Made By: Aadim Gyawali
Publish Date: 1/16/2023
'''

import sys

sys.set_int_max_str_digits(999999999)

def pair(input_str):
    paired_array = []
    for i in range(0, len(input_str), 2):
        if i + 1 < len(input_str):
            paired_array.append(input_str[i:i + 2])
    return paired_array

def make_pairs(input_str):
    paired_array = []
    if '.' in input_str:
        int_part, frac_part = input_str.split('.')
        if len(int_part) % 2 == 1:
            int_part = '0' + int_part
        if len(frac_part) % 2 == 1:
            frac_part = frac_part + '0'
        paired_array.extend(pair(int_part))
        paired_array.append('.')
        paired_array.extend(pair(frac_part))
    else:
        if len(input_str) % 2 == 1:
            input_str = '0' + input_str
        paired_array = pair(input_str)
    return paired_array

def calculation(num, side_num, index):
    num = int(num)
    side_num = int(side_num)
    index = int(index)
    if index == 0:
        sq_num = 0
        while sq_num * sq_num <= num:
            sq_num += 1
        sq_num -= 1
        side_num = int(str(sq_num + sq_num) + "0")
        sub_value = num - (sq_num * sq_num)
        return side_num, sub_value, sq_num
    else:
        sq_num = 0
        while (side_num + sq_num) * sq_num <= num:
            sq_num += 1
        sq_num -= 1
        sub_value = num - ((side_num + sq_num) * sq_num)
        side_num = int(str((side_num + sq_num) + sq_num) + '0')
        return side_num, sub_value, sq_num

def user_input(msg):
    while True:
        try:
            inp = float(input(msg))
            return inp
        except ValueError:
            print("Please enter a valid input.")

def main(inp, decimal_points):
    list_of_numbers = make_pairs(str(inp))
    part = "int"
    side_num = 0
    sub_value = 0
    final = ""
    sq_num = 0
    for index, pair in enumerate(list_of_numbers):
        if index == 0:
            num = pair
        else:
            num = str(sub_value) + pair
        if (len(list_of_numbers) == index + 1 and part == "int") or pair == ".":
            final += "."
            number_of_pairs_after_decimal_point = len(list_of_numbers[list_of_numbers.index(".") + 1:])
            total_decimal_points = decimal_points - number_of_pairs_after_decimal_point
            part = "frac"
            if pair == ".":
                continue
        if part == "frac" and total_decimal_points > 0:
            list_of_numbers.append("00")
            total_decimal_points -= 1

        side_num, sub_value, sq_num = calculation(num, side_num, index)
        final += str(sq_num)
    return(final)
    # print(f"The square root of {inp} is approximately {final}")

if __name__ == '__main__':
    input_value = (user_input("Enter the number to find the square root of: "))
    decimal_points = int(user_input("Enter the number of decimal points: "))
    print(main(input_value, decimal_points))
