#input a number that is greater than 1
n = int(input("Enter the value of n: "))

#print the numbers from 1 to n
print("numbers from {0} to {1} are: ".format(n,1))

#loop to print numbers
for i in range(n,0,-1):
    print(i)