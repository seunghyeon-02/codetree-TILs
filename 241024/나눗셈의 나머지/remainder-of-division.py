arr = input()
arr = arr.split()
a = int(arr[0])
b = int(arr[1])

n_arr= []
sum = 0

while a > 1:
    c = a % b
    a = a // b
    n_arr.append(c)

for i in range(b):
    k = n_arr.count(i)
    sum += k * k

print(sum)