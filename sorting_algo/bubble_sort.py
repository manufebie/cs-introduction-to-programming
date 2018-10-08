# Bubble sort

LIST = [2,4,3,5,1]

print('Original list: {}'.format(LIST))
print()

def bubble_sort(sort_me):
    N = len(sort_me) # determine length of list

    for k in range(1, N): # current itteration

        for j in range(N - k): # total comparisons
            
            if sort_me[j] > sort_me[j+1]:
                # code that bubbles up the element
                hold = sort_me[j]
                sort_me[j] = sort_me[j+1]
                
                sort_me[j+1] = hold
        print('{}'.format(sort_me))

bubble_sort(LIST)


print()
print('Result is: {}'.format(LIST))
