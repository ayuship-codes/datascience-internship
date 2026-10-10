#check even/odd
def evenOdd(num):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


#check prime number
def isPrime(num):
    flag = 0
    for i in range(2,num):
        if num%i==0:
            flag = 1
            break
        

    if flag==1:
        print(f"{num} is not prime")        
    else:
        print(f"{num} is prime")



num = int(input("enter the number to check even/odd: "))
evenOdd(num)
isPrime(num)