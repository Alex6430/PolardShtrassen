import math
import random


def find_Poly(N):
    result = []
    i = 0
    while (not(ferma(N))):
        result.append(Pollard_Shtrasen(N))
        N //= result[-1]
        i+=1
    result.append(N)
    return result

def str_Poly(mass):
    poly = ''
    for i in range(len(mass)):
        if(i==len(mass)-1):
            poly += str(mass[i])
        else:
            poly += str(mass[i]) + '*'
    return poly


def Pollard_Shtrasen(N):
    z = int(pow(pow(N,0.5),0.5))+1
    fun_F = [1]*z
    for i in range(1,z+1,1):
        for j in range(1,z+1,1):
            fun_F[i-1] *= ((i-1)*z+j)
            fun_F[i-1] %= N
            if(fun_F[i-1]==0):
                fun_F[i - 1]=0
                break
        gcd_val = gcd(N,fun_F[i-1])
        if(gcd_val>1):
            if(i==1):
                for m in range(2, z + 1, 1):
                    if(gcd_val%((i - 1) * z + m)==0):
                            return ((i - 1) * z + m)
            else:
                for m in range(1, z + 1, 1):
                    if(gcd_val%((i - 1) * z + m)==0):
                            return ((i - 1) * z + m)
            # return gcd(N,fun_F[i-1])


def input_value():
    print("Введите число:")
    n = int(input())
    while True:
        if n > 0:
            return n
        print("Вы ввели неверное число. Введите заново")
        n = int(input())


def is_simple(num):
    i=2
    limit = math.sqrt(num)
    while i <= limit:
        if num % i == 0:
            return False
        i += 1
    return True

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

def ferma(num):
    if num == 2 or num == 3:
        print("Число " + str(num) + " простое")
        return True

    for i in range(50):
        a = random.randrange(2, num - 1)

        if not gcd(a, num) == 1:
            print("Число " + str(num) + " составное")
            return False

        b = pow(a, num - 1, num)
        if not b == 1:
            print("Число " + str(num) + " составное по основанию " + str(a))
            return False

    print("Число " + str(num) + " простое")
    return True

# print(find_Poly(input_value()))
#print(ferma(input_value()))
