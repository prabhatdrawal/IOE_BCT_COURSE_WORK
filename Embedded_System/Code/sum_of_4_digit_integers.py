''''
def main():
    n = input("enter the four digit integer : ")
    sum = 0   # variable initialized to store the sum
    for i in range (0,4): # loop run from 0 to 3
       sum = int(n[i]) + sum

    print(f"the sum of four integer data is as :{sum} ")

main()
'''

# for indexing you need integer and int object is not subscriptable
# str is by default set ; can't be indexed 
def main():
    n = input("enter the four digit integer : ")
    sum = int(0) # variable initialized to store the sum
    i = 3
    while(i!= -1):
        sum = int(n[i]) + sum
        i -= 1

    print(f"the sum of the four integer data is as : {sum}" )

main()