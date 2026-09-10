"""
write a program to display sum of number from  1 to n
"""

def sum_number(number):

    total = 0

    for i in range(1,number +1):

        total = total + i

    print(total)

sum_number(5)    
         