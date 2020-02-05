row=int(input("Enter number of rows for the tree : "))

for j in range(0,row+1):
    for k in range(0,row-j):
        print(" ",end="")
    for i in range(0,j):
        print("*",end="")    
    print()
    