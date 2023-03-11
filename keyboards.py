#linear search
def linear_search(arr, value):
    for item in range(len(arr)):
        if value == arr[item]:
            return item
    return -1

arr = ['a', 'b', 'c', 'd', 'g', 'o', 'v']
value = 'o'
print(linear_search(arr, value))
