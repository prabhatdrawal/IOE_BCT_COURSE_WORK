def main():
    n = input("enter the four digit integer number : ")
    i = 3
    max_digit = n[i]
    while i >= 0:
        if(n[i] > max_digit):
            max_digit = n[i]
        i -= 1
    print(f"maximum digit is :{max_digit}")

main()
