'''
Made By: Aadim Gyawali
Publish : 1/16/2023
Date
'''
import sys
sys.set_int_max_str_digits(999999999)
def make_pairs(string):
    result = []
    if len(string) % 2 != 0:
        result.append(string[0])
        string = string[1:]
    for i in range(0, len(string), 2):
        result.append(string[i:i + 2])
    return result
def div(value, side_num):
    z = 0
    while (side_num + z) * z <= value:
        z = z + 1
    z = z - 1
    return side_num + z, z
def max_square_subtraction(num):
    num = int(num)
    if num!=0:
        square_number = closest_qrt(num)
    else:
        square_number=0
    side_num = (square_number + square_number) * 10
    sub_value = num - square_number**2
    return side_num, sub_value, square_number
def closest_qrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def main():

    try:
        inp = float(input("Enter a number: "))
    except:
        print(f'''ValueError: invalid literal for number. ''')
        main()
    if str(inp).split(".")[1]=="0":
        inp=int(str(inp).split(".")[0])
    else:
        num1=int(str(inp).split(".")[0])
        num2=str(inp).split(".")[1]
        if len(num2)%2!=0:
            num2=int(num2)*10
    if type(inp)==float:
        list_of_numbers = make_pairs(str(num1))
        list_of_numbers2= make_pairs(str(num2))
        list_of_numbers.extend(".")
        list_of_numbers.extend(list_of_numbers2)
    else:
        list_of_numbers = make_pairs(str(inp))
        ex=list_of_numbers
    first = list_of_numbers.pop(0)
    side_num, sub_value, final = max_square_subtraction(first)
    i=0
    deci=1
    if type(inp)==float:
        try:
            deci=int(input("Enter a No of Decimals: "))
        except:
            print(f'''ValueError: invalid literal for number.''')
            main()
        if deci > 100:
            print(f'''ValueError: Exceeds the limit (100) for integer.''')
            main()
    a=False
    dot=False
    while len(list_of_numbers) != 0 and i!=deci:
        first = list_of_numbers.pop(0)
        if first==".":
            final=str(final)+"."
            dot=True
            a=True
            continue
        value = int((str(sub_value) + str(first)))
        side_num, final1 = div(value, side_num)
        final = (str(final) + str(final1))
        sub_value = value - side_num * final1
        side_num = (side_num + final1) * 10
        if dot==True:
            i=i+1
    if sub_value!=0:
        if type(inp)==int:
            try:
                deci=int(input("Enter Quantity Of Decimals: "))
            except:
                print("ValueError: invalid literal for number.")
                main()
            if deci <0:
                print("ValueError: Exceeds the limit (100) for integer.")
                main()
        while i != deci: 
            if sub_value != 0:
                value = int(str(sub_value) + str("00"))
                side_num, final1 = div(value, side_num)
            if a==False:
                final = (str(final) + "." + str(final1))
                a = True
            elif a==True:
                final=(str(final)+(str(final1)))
            else:
                final = (str(final) + str(final1))
            sub_value = value - side_num * final1
            side_num = (side_num + final1) * 10
            i = i + 1

    print(f"The square root of {inp} is {final}")
    ask=2
    while ask!=1:
        ask=input("Do you want to continue(y/n): ")
        if ask.lower()=="y":
            main()
            ask=1
        elif ask.lower()=="n":
            print("Thank you for using!")
            exit()
            ask=1
        else:
            print(f'ValueError: "{ask}" not defined')
            ask=2

main()