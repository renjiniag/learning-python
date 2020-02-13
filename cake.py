def max_duffel_bag_value(lst,max):
    dict2={}
    list2=[]
    for a,b in lst:
        div=int(b/a)      
        dict2[div]=(a,b)
        list2.append(div)
    list2.sort(reverse=True)
    sum1=0
    cake1=0
    i=0
    while max>0 :
        a1,b1=dict2[list2[i]]
        cake1=int(max/a1)
        if cake1>0:
            sum1=sum1+b1*cake1
            max=max%a1
        else:
            i=i+1      
    print(sum1)
         
cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

# Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
max_duffel_bag_value(cake_tuples, capacity)