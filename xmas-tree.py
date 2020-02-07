row=int(input("Enter number of rows for the tree : "))

for j in range(row,0,-1):
    for k in range(row-j,0,-1):
        print(" ",end="")
    for i in range(j,0,-1):
        print("*",end="")    
    print()
    for k in range(row-j+1,0,-1):
        print(" ",end="")
    for m in range(j-1,0,-1):
        print("-",end="")
    print()
    
