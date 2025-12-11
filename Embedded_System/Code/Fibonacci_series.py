def main():
    x = 0
    y = 1
    count = 1
    n = int(input("enter the term upto display the series: "))
    print(f"{x}\n")
    print(f"{y}\n")
    while(count<=(n-2)):
        z = x+y
        x = y
        y = z 
        count += 1
        print(f"{z}\n")
main()