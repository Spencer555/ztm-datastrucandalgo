
# linear search
# this goes through the list one by one in order till we find what we are looking for and returns none if nothing is found and its the end of list
beasts = ["Centaur", "Godzilla", "Mosura", "Minotaur", "Hydra", "Nessie"]


beasts.index("Godzilla")
print(beasts.index("Godzilla"))


for i in beasts:
    if i == 'Godzilla':
        print(True)


# binary search is there a better way to find if its sorted we divide the list into 2 and check if the items we are searching if its higher or less then we discard then we do until we find the item this is 0(logn)

numbers = [1, 4, 6, 9, 12, 34, 45]


def binary_search(n, arrays):
    mid_point = round(len(arrays)/2)
    first_half = numbers[:mid_point]
    second_half = numbers[mid_point:]

    while n:
        if n == numbers[mid_point]:
            return f' {n} found'

        if n > numbers[mid_point]:
            mid_point = round(len(first_half)/2)
            first_half = numbers[:mid_point]
            second_half = numbers[mid_point:]

        elif n < numbers[mid_point]:
            mid_point = round(len(first_half)/2)
            first_half = numbers[:mid_point]
            second_half = numbers[mid_point:]
            return binary_search()


print(round(len(numbers)/2))

print(numbers[4])
print(numbers[4:])
