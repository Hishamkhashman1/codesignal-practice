numbers = [5,5,5]


# if numbers in even indices are increasing monotonically, then return increasing
# if numbers in even indices are decreasing monotonically, then return decreasing 
# othersise, return None

def solution(numbers):
    even_list = []
    for i in range (len(numbers)):
        if i % 2 == 0:
            even_list.append(numbers[i])
    
    increasing = True
    decreasing = True

    if len(even_list) < 2:
        increasing = False
        decreasing = False
    else:
        for j in range (len(even_list)-1):
                if even_list[j] > even_list[j+1]:
                    increasing = False
                if even_list[j] < even_list[j+1]:
                    decreasing = False
                if even_list[j] == even_list[j+1]:
                    increasing = False
                    decreasing = False
    
    if increasing == True:
        return "increasing"
    if decreasing == True:
        return "decreasing"

    return None


print (solution(numbers))
            
