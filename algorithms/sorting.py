'''
when it comes to sorting if u are not implementing it know how it works 
'''

'''
type of sorts 
these are elementary sorts they are basic simple sorting algo you would think of if someone asks you to sort something at the top of yr head 
(
bubble sorts
insertion sort 
selection sort
)

they are complex algo that are more effiecient
(
mergesort
quick sort
)
'''


'''
bubble sorts
6,5,3,1,7

so we look at 6 and 5 
then 6 is larger then 5 the we swap positions 
5,6
then we compare 6 and 3 
5,3,6
then we compare 6 and 1
5,3,1,6
then we compare 6 and 7
5,3,1,6,7
we start again it the list is completely sorted
'''

# it is simple but least efficient its o(n^2) for item and space o(1)


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def bubbleSort(array):
    length = range(len(array)-1)
    for i in length:  # then we start again
        for j in length:  # we bubble things up in the list
            if (array[j] > array[j+1]):
                # swap numbers
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


# bubbleSort(numbers)
print(numbers)
# alternative code


def bubblesort1(arr):
    qw = 0
    while qw < len(arr):
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        qw += 1
    return arr


# selection sort
'''
it scans the list of element for the smallest number and places it at the first element then we start again till the list is sorted
'''


def selectionSort(array):
    i = 0
    while i < len(array):
        min = array[i]
        index = i

        for j in range(i+1, len(array)):
            if array[j] < min:
                index = j
                min = array[j]

        array[i],  array[index] = array[index], array[i]
        i += 1

    return array


# selectionSort(numbers)
# print(numbers)


# insertion sort
'''
it is usefull for times when u re sure the list is pretty sorted  or its already sorted 



'''

'''
6,5,3,1,8,7,2,4

we keep 6 in position 
then we look at the next item 5 
because it is less than 5 we switch it over 
then we compare 3 to 5 and 6 it is less than that so we switch it over to the first
then so on till its sorted 
its good for small data sets
'''

'''
check if the first item is greater than next then swap
'''


def insertionSort(array):
    qs = 0
    length = len(array)
    while qs < length:
        for i in length:
            pass
        qs += 1
