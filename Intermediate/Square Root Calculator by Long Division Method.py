'''
Made By: Aadim Gyawali
Publish Date: 1/16/2023
'''

import sys
sys.set_int_max_str_digits(999999999)
def pair(input_str):
    paired_array = []
    for i in range(0, len(input_str), 2):  # Iterate over the string in steps of 2
        if i + 1 < len(input_str):  # Ensure there's a valid pair to process
            paired_array.append(input_str[i:i + 2])  # Add a pair of characters to the array
    return paired_array
def make_pairs(input_str):
    paired_array = []
    if '.' in input_str:
        int_part, frac_part = input_str.split('.')  # Separate integer and fractional parts
        if len(int_part) % 2 == 1:  # Check if integer part length is odd
            int_part = '0' + int_part  # Pad with a leading zero
        
        if len(frac_part) % 2 == 1:  # Check if fractional part length is odd
            frac_part = frac_part + '0'  # Pad with a trailing zero
        
        paired_array.extend(pair(int_part))  # Add integer part pairs
        paired_array.append('.')  # Add the decimal point
        paired_array.extend(pair(frac_part))  # Add fractional part pairs
    else:
        if len(input_str) % 2 == 1:  # Check if input length is odd
            input_str = '0' + input_str  # Pad with a leading zero
        paired_array = pair(input_str)
    return paired_array
def calculation(num, side_num, index):
    num=int(num)
    side_num=int(side_num)
    index=int(index)
    if index == 0:  # Check if it's the first time
        sq_num = 0
        while sq_num * sq_num <= num:  # Find the closest square root of a number
            sq_num += 1
        sq_num -= 1
        side_num = (sq_num + sq_num) * 10  # Calculate the side number for the first time
        sub_value = num - (sq_num * sq_num)  # Calculate the sub value for the first time # Storing values in a list
        return side_num, sub_value, sq_num
    else:  # When it's not the first time
        sq_num = 0
        while (side_num + sq_num) * sq_num <= num:  
            # Find such that (side_num + sq_num) * sq_num <= num
            sq_num += 1
        sq_num -= 1  # sq_num is the square number
        sub_value = num - ((side_num + sq_num) * sq_num)  
        # sub_value = num - (side_num + sq_num) * sq_num
        side_num = ((side_num + sq_num) + sq_num) * 10  # Storing values in a list
        return side_num, sub_value, sq_num
def userinput(msg):
    while True:
        try:
            inp=float(input(msg))
            break
        except:
            print("Please enter a valid input.")
    return inp
def sqcal(inp,decimalPoints):
    if inp:
        inp=userinput("Enter a number: ")
    listOfNumbers=make_pairs(str(inp))
    part="int"
    sideNum=0
    subValue=0
    final=""
    sqNum=0
    for index, pair in enumerate(listOfNumbers):
        if index==0:
            num=pair
        else:
            num=str(subValue)+pair
        if ( len(listOfNumbers)==index+1 and part=="int" ) or pair==".":
            final=final+"."
            if decimalPoints:
                decimalPoints=userinput("Enter Number of decimal Points: ")
            numberOfPairsAfterDecimalPoint = len(listOfNumbers[listOfNumbers.index(".") + 1:])
            for j in range(int(decimalPoints-numberOfPairsAfterDecimalPoint)):
                listOfNumbers.append("00")
            part="frac"
            if pair==".":
                continue
        sideNum,subValue,sqNum=calculation(num,sideNum,index)
        final=final+str(sqNum)

    print(f"The square root of {inp} is {final}")
    while True:
        ask=input("Do you want to continue(y/n): ")
        match ask.lower():
            case "y":
                sqcal(True,True)
            case "n":
                print("Thank you for using !")
                exit()
            case default:
                print("Please enter a valid input.")
                pass
if __name__=="__main__":
    sqcal(True,True)
'''
Use sqcal(number, decimal_points) to find the square root of a number
'''