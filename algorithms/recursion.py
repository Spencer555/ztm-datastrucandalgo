'''
they are functions that programmers write 

data struc and algo create programs 

important algos 
sorting 
dynamic programming 
bfs + dfs (searching)
recursion

'''

'''
recursion is not techically an algorithm but more of a concept

a function that refers to itself inside a function

of a function that calls itself 


def inception():
    inception()
    
its good for tasks that have repeated subtasks to do


the posible problem with recusion is the computer needs to allocate memory to remember stuff stack overflow can ocurr were there is no base case to stop it
'''

'''
a recursive function has two part 
the recursive part( the one that calls the function and tells it to keep running)

then the base case (quit the function there is nothing more to search )
'''


def inception(counter):
    print(counter)
    if counter > 3:
        return "done"
        # now we have a return keyword but it does not return done because it keeps removing things from the call stack popping of every stack prev saved
        # so u have to bubble up to the top
    counter += 1
    # as soon as it hits here it goes back to the top of the function anything after wont run
    # inception(counter)

    # this is how u bubble up u return the recursive case
    return inception(counter)


# inception(0)


'''
steps 
identify the base case 
identify the recursive case 
get closer and closer and return when needed, usually u have only two returns 
'''

# Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop

'''
factorial 
5! = 5 * 4 * 3* 2 *1
'''


def findFactorialRecursive(number):
    # code here
    if number == 0:
        return 1
    return number * findFactorialRecursive(number - 1)


def findFactorialIterative(number):
    answer = 1
    for i in range(1, number+1):
        answer = i * answer
    return answer


print(findFactorialIterative(10))
print(findFactorialRecursive(10))


# fibonacci sequence
'''
0,1 1,2,3,5,8, 13, 21, 34, 55, 89, 144
the pattern of the sequence is that each value is the sum of the two prev values that means n=5 is 2 + 3
'''


def fibonacciIterative(n):
    if n < 2:
        return n
    first = 0
    second = 1
    third = 0
    for _ in range(1, n):
        third = first + second
        first = second
        second = third

    return third


def fibonacciRecursive(n):
    if n < 2:
        return n
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)


print('fd', fibonacciIterative(10))
print('fd', fibonacciRecursive(10))


'''
anything that can be implemented iteratively can be done recursively 

there are times where recursion can keep ur code dry 
and allow ur code to be more readable 

but it has a large stack(extra memory footprint because each time we add a function it adds a layer of memory)

u want to avoid recursion when memory is expensive


iterative approach may not be readable but does not take huge memory


we use recursion when working with datastruc which we dont know how deep they are e.g trees and graphs


tail call optimization - this allows recursion to be called without increasing call stack
'''

'''
when to use recusion
complex problems like traversing or searching through a tree or graph 

sorting through items in some cases


rules to follow 
every time you are using a tree or converting something into a tree, consider recursion

three things that might trigger a recursive approach
1 divide into a number of subproblems that are smaller instances of the same problem

2 each instance of the subproblem is identical in nature 

3 the solutions of each subproble can be combined to solve the problem at hand 

a lot of divide and conquer questions uses recursion

the one thing recursion can do that looping can't is that they make tasks easier interms of readablity and coding

recursion can be costly because recursion and space complexity are not friends

recursion 
merge sort 
quick sort 
tree traversal 
graph traversal
'''


# reverse string


def reverseString(str):
    '''
    change to array reverse and change back to string 
    '''

    if len(str) > 0:
        split = list(str)
        return "".join(split[::-1])
    return 'string is empty'


def reverse(word):
    size = len(word)
    if size == 0:
        return
    last_char = word[size-1]
    print(last_char, end='')
    return reverse(word[0:size-1])


reverse('hello there')

print(reverseString("yoyo master"))
