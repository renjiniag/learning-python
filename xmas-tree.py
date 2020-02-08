row=int(input("Enter number of rows for the tree : "))

for j in range(row,0,-1):
    for k in range(row-j,0,-1):
        print(" ",end="")
    for i in range(j,0,-1):
        if i==1:
            endline="\n"
        else:
            endline="_"
        print("*",end=endline)    
           
''' Output
Enter number of rows for the tree : 4
*_*_*_*
 *_*_*
  *_*
   *
'''   
