def main():
   x = int(input(" enter the value of the x "))
   y = int(input(" enter the valus of the y "))
   while(x!=y):
         if(x>y):
            x= x-y
         else:
            y = y-x    

   print(f"the HCF of the given numbers is :{x}")      

main()
