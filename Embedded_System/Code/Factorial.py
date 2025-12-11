def main():
    n = int(input(" enter the number : "))
    r = 1
    while(n!=0):
        r =r * n
        n -= 1

    print(f" the factorial is : {r}")

main()