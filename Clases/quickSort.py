vector = [9,8,7,6,5,4,3,2,12]
vector2 = [1,2,3,4,5,6,7]

def quickSort(vector,first,last):
    pivot = last
    left = first
    right = last - 1
    while(left < right):
        while((vector[left] < vector[pivot]) and (left<=right)):
            left += 1
        while(vector[right] > vector[pivot] and right>=left):
            right -=1
        if(left < right):
            # Intercambia valores
            vector[left],vector[right] = vector[right],vector[left]
    if(vector[pivot] < vector[left]):
        vector[pivot],vector[left] = vector[left],vector[pivot]
    if(left-first > 1 ):
        quickSort(vector,first,left-1)
    if(last>left):
        quickSort(vector,left+1,last)
    
quickSort(vector,0,len(vector)-1)
vector2.sort()
print(vector)
print(vector2)

