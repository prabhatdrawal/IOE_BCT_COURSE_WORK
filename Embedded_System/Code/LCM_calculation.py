def main():
    x = int(input("enter the value of x : "))
    y = int(input("enter the value of y : "))
    z = x * y 
    while(x!=y):
        if(x>y):
            x = x-y
        else:
            y = y-x
    HCF = x
    LCM = int(z / HCF )
    print(f" The lcm of the given values is : {LCM}")

main()