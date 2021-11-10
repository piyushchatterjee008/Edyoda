#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Fibonacci series between 0 to 50

'''
Note : The Fibonacci Sequence is the series of numbers :

0, 1, 1, 2, 3, 5, 8, 13, 21, ....

Every next number is found by adding up the two numbers before it.

Expected Output : 1 1 2 3 5 8 13 21 34

'''

first=0
second=1

print(first)

while(second<=50):
    print(second)
    first,second=second,first+second


# In[2]:


#Write a Python program that accepts a word from the user and reverse it.

'''
Sample Test Case

Input : Edyoda
output: adoydE
'''


User_input = input("Enter any word :")

print("Reverse of your word is :",User_input[::-1])


# In[6]:


#Write a Python program to count the number of even and odd numbers from a series of numbers.

'''
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :

Number of even numbers : 5
Number of odd numbers : 4
'''



list_series =[1, 2, 3, 4, 5, 6, 7, 8, 9]
count_e=0
count_o=0
for i in list_series:
    if (i%2!=0):
        #print("Numberic",i, "is odd")
        count_o=count_o+1
    else:
        #print("Numberic",i, "is even")
        count_e=count_e+1
print("Number of even numbers :",count_e)
print("Number of odd numbers :",count_o)


# In[ ]:




