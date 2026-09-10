"""
write a program to display product of number from  1 to n
"""

def product_number(number):

    product = 1

    for i in range(1,number+1):

        product = product * i

    print(product)

product_number(5)            