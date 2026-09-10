"""
write a program chk number is prime or not

"""

def prime_number(number):

    for i in range(2,number):

        if number % i == 0:
         print("Not prime number")
         break

    else:print("Prime number")

prime_number(7)