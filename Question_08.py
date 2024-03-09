array =  [23, 22, 24,8, 9, 10]
n = len(array)

leaders = []
max_right = float('-inf')

for i in range(n-1, -1, -1):
    if array[i] > max_right:
        leaders.append(array[i])
        max_right = array[i]

print("Leaders in the sequence:", leaders[::-1])