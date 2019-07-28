# Lexicographical Order
# Problem Statement:
# You are given a string array named arr, of size N, containing KEYS and VALUES separated by a space.
# Your task is to find, for each unique KEY, the number of VALUES with that key and the VALUE with the highest 
# lexicographical order (also called alphabetical order OR dictionary order).

# (Have a look at the sample test cases for more clarity.)
# Sample Input 1:
# arr = [
#    “key1 abcd”,
#    “key2 zzz”,
#    “key1 hello”,
#    “key3 world”,
#    "key1 hello"
# ]

# Sample Output 1:
# One possible output (you can return strings in any order):
# [
#    "key1:3,hello",
#    "key2:1,zzz",
#    "key3:1,world"
# ]
# Sample Test Case 2:
# Sample Input 2:
# arr = [
#    “mark zuckerberg”,
#    “tim cook”,
#    “mark twain”
# ]
# Sample Output 2:
# One possible output (you can return strings in any order):
# [
#    "mark:2,zuckerberg",
#    "tim:1,cook"
# ]


arr = [
   'key1 abcd',
   'key2 zzz',
   'key1 hello',
   'key3 world',
   'key1 hello'
]

def solve(arr):
    keys = {}
    for raw_val in arr:
        key, value = raw_val.split(' ')
        values = keys.get(key, [])
        values.append(value)
        keys[key] = values
    output = []
    for key in keys:
        keys[key].sort()
        out_val = "{key}:{count},{highest}".format(key=key, count=len(keys[key]), highest=keys[key][-1])
        output.append(out_val)
    return output

arr1 = [
   'mark zuckerberg',
   'tim cook',
   'mark twain'
]
solve(arr1)

solve(arr)