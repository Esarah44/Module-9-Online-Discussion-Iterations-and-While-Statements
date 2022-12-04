#While Loop and counter
#Sara Hernandez
#November 22,2022
#While loop will initialize a counter at 0 and will run until the counter reaches 50


tens = []
num = 20

while num <= 70:
    if num % 10 == 0:
        tens.append(num)
    num += 1

print(tens)