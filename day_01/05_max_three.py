

"""
write a program to print largest of three numbers

"""

def max_of_numbers(num1,num2,num3):

    if num1 > num2 and num1 > num3:
        print(f"Largest Number = {num1}")

    elif num2 > num1 and num2 > num3:
        print(f"Largest Number = {num2}")

    else:print(f"Largest Number = {num3}")        

max_of_numbers(10,500,100)