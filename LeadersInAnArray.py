def LeadersInarray(array):
    
    leaders = []
    max_element = float('-inf')  

   
    for i in range(len(array)-1, -1, -1):
        if array[i] > max_element:
            leaders.append(array[i])
            max_element = array[i]

    leaders.reverse() 
    return leaders




array=list(map(int,input().split()))
print(LeadersInarray(array))