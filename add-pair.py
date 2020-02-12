n=int(input("How many numbers do you want in the list : "))
print("Enter the numbers")
lst=[]
for i in range(0,n):
    num=int(input())
    lst.append(num)

add=int(input("Enter the number you want the sum as : "))
ans=[(x,y) for x in lst for y in lst[int(n/2)::] if x+y==add]
if len(ans)!=0:
    print(ans)
else:
    print("Sorry. Couldnt find any pairs")