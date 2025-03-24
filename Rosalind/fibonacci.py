def Fibonacci_Loop(number):
    old=l
    new=l
    for itr in range(number-1):
        tmpval=new
        new=old
        old=old+tmpval
    return new
def Fibonacci_Loop_Pythonic(number):
    old,new=1,1
    for itr in range(number-1):
        new,old=old+new
    return new

print(Fibonacci_Loop(13))
print(Fibonacci_Loop_Pythonic(12))