print("welcome")

number=[15,89,55,88,79,50]


largest = number[0]

for num in number:
    if num > largest:
        largest = num

print("Largest number:", largest)

Snum = [45, 30, 22, 11, 45, 89]

smallest = Snum[0]

for small in Snum:
    if small < smallest:
        smallest = small

print("Smallest number:", smallest)