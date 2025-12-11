def main():
    x = int(input("enter the value of the base: "))
    n = int(input(" enter the exponential {power} value of base:"))
    r = 1

    while(n!=0):
        r = r * x 
        n -= 1

    print(f"the final obtained vallue is : {r}")

main()