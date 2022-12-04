#While Loop
#Sara Hernandez
#November 22,2022
#The while loop should append the current value of a counter variale to a list and then increase the counter by 1


L = list()
counter = 0
while counter < 21:
    L.append(counter)
    counter += 1

print(L)