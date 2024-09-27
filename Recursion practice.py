#Recursion practice 

def find_sum(number):
    if number == 0:
        return number
    else:
        return number + find_sum(number - 1)
    
print(find_sum(10))

#Without recursion
def find_sum2(num):
    result = 0
    for i in range(1, num + 1):
        result = result + i
    return result

print(find_sum2(3))

#Factorial
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))

#Without recursion
def fact2(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(fact2(5))