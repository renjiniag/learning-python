
for i in range (6,0,-1):
    for j in range (0,i):
        if i-j==1:
            endline='\n'
        else:
            endline=''
        print('*',end=endline)