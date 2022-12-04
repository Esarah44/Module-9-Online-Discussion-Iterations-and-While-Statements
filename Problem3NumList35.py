#While Loop and sum
#Sara Hernandez
#November 22,2022
#Continue adding numbers until the sum of the list of the numbers is greater than 100


total_num = 0

while total_num <= 100:
    num = input('Enter positive integer: ')
    total_num += int(num)
    print('Current sum is',total_num)
