#  memoization
# dynamic programming is just an optimization technique using caching

# its a way to solve problems by breaking it down to a collection of sub problems solving each of those subproblems once and storing thier solution incase it occurs nextime

# caching is a way to store values so u can use it later on and memoization is a specific form of cahcing we would be talking about and we use it a lot in dynamic programming


def addTo80(num):
    return num+80


# print(addTo80(5))
# print(addTo80(5))
# print(addTo80(5))


cache = {}


def memoizedAddTo80(num):
    # if we have cached it before return the cached item else calculate it
    if num in cache:
        print('short time')
        return cache[num]

    else:
        print('long time')
        cache[num] = num+80
        return cache[num]


# print(memoizedAddTo80(9))
# print(memoizedAddTo80(9))

# its good to have the cache live inside the function not a global scope but the cache would reset everytime we call the function to get around this we use closures in


def memoizedAddTo80_closure():
    # if we have cached it before return the cached item else calculate it
    cache = {}

    def memoized(num):
        if num in cache:
            print('short time')
            return cache[num]
        else:
            print('long time')
            cache[num] = num+80
            return cache[num]

    return memoized


memo = memoizedAddTo80_closure()
# print(1, memo(7))
# print(2, memo(7))


# u can think of dynamic programing as divide and conquer + memoization
'''
1 can the problem be divided in to sub problems 
2 recursive solution 
3 are there repetitive sub problems 
4 memoize subproblems 
5 demand a raise from your boss 
'''


calculations = 0

cache = {
    'steps': 0
}

pra = []


def fib(n):
    cache['steps'] += 1

    if n in cache:
        return cache[n]

    elif (n < 2):
        cache[n] = n
        return cache[n]
    else:
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]


print(fib(10))
print(cache['steps'])


12 solution insertion sort
