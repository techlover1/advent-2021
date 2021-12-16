values = open('p01-input.txt')

valuelist = values.read().split()

counter = 0

for i in range(len(valuelist)):
    if int(valuelist[i]) > int(valuelist[i-1]) and i != 0:
        counter +=1

print(f'Total count: {counter}')