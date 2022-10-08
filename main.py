# Author: Jasmine Singh
# Github username: Jassig98
# Date: 10/6/2022
# Description: change.py

print("Please enter an amount in cents less than a dollar.")
num_1=int(input())
print("Your change will be:")
print("Q:",num_1//25)
num_1= num_1 % 25
print("D:" ,num_1//10)
num_1= num_1 % 10
print("N:" ,num_1//5)
num_1= num_1 % 5
print("P:" ,num_1//1)
num_1= num_1 % 1