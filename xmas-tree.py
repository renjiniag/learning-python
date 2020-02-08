for j in range(row,0,-1):
    for k in range(row-j,0,-1):
        print(" ",end="")
    for i in range(j,0,-1):
        print("*",end=" ")    
    print()
    for k in range(row-j+1,0,-1):
        print(" ",end="")
    for i in range(j,1,-1):
        print("-",end=" ") 
    print()

    ''' Output
Enter number of rows for the tree : 4
* * * *
 - - -
 * * *
  - -
  * *
   -
'''   
