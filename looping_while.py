# write a program to print hello python 3 time iteration completed

# i=1
# while i <=3:
#     print("hello world")
#     i=i+1
# else:
#     print("iteration completed")


# write a program print sequence of number from 1 to 5 
# i=1
# while i <=5:
#     print(i , end =' ')   #it is print horizontaly
#     # print(i) // it will print as verticaly
#     i=i+1

# write a program sequence number 5 to 1
# i=5
# while i >=1:
#     print(i , end =' ') 
#     i=i-1

# write program to print even number from 1 to 10
# i=1
# while i<=10:
#     if i%2==0:
#         print(i,end=' ')
#     i=i+1
# other way
# i=2
# while i<=10:
#     print(i,end=' ')
#     i=i+2

# write a program to print odd number 1 to 10
# i=1
# while i<=10:
#     if i%2==1:
#         print(i,end ='')
#     i =i+1

# write a program to print multiplication data of given number
# num=5
# i=1
# while i<=10:
#     print(f'{num} * {i} : {num*i}')
#     i=i+1
# program to find sum of 5 natural number [1+2+3+4+5]
# i=1
# sum=0
# while i<=5:
#     sum=sum+i
#     i=i+1
# print(f'sum of 5 natural num {sum}')
# print(sum)

# write a program to find factorial of given number 
# num=5
# fact = 1
# i=1
# while i<=num: # instead of num direct write 5 
#     fact = fact * i
#     i=i+1
# print(fact)


# write a progrm to find sum of even sum and sum of odd num , product of even number and product of
#  odd number from 1 to 10
# i=1
# even=2
# odd=1
# product_even=1
# product_odd=1
# while i<=10:
#     if i%2==1:
#         even = even + i
#         product_even = product_even * i
#     elif i%2==0:
#         odd=odd+i
#         product_odd=product_odd*i
#     i=i+1
# print(even)
# print(odd)
# print(product_even)
# print(product_odd)


# write program digit evn num
# num=298
# count =0
# while num > 0:
#     digit = num % 10
#     if digit%2==0:
#         count = count + 1
#     num = num // 10
# print(count)

# other way
# num=298
# count =0
# while num > 0:
#     if num%2==0:
#         count = count + 1
#     num = num // 10
# print(count)

# program evn digit num odd digit from given number
# num=38792
# even_count=0
# odd_count=0
# while num > 0:
#     digit = num % 10
#     if digit % 2==0:
#         even_count =even_count + 1
#     else:
#         odd_count = odd_count + 1
#     num =num // 10
# print(f'even_digit: {even_count}')
# print(f'odd digit :{odd_count}')

# write a program even digit from num
# num=38792
# while num > 0:
#     digit = num%10
#     if digit % 2==0:
#         print(f'{digit} is a even digit')
#     num =num //10

# write a program to print even digit odd digit from given number
# num=38792
# while num > 0:
#     digit = num%10
#     if digit % 2==0:
#         print(f'{digit} is a even digit')
#     elif digit % 2!=0:
#         print(f'{digit} is an odd digit')
#     num =num //10

# write a program to find number of element present in given list
# list=[98,80,45,30]
# i=0
# while i < len(list):
#     i=i+1
# print(i)

# write a program num of character present in given string
# string="python"
# i=0
# while i< len(string):
#     i =i + 1
# print(i)

# program print even number list collection
# list=[37,78,12,67,53,99]
# i=0
# while i<len(list):
#     if list[i]%2==0:
#         print(f'{list[i]} is an even num')
#     i=i+1

# //write a program from list collection and find num of even number
# list=[37,78,12,67,53,99]
# i=0
# count =0
# while i<len(list):
#     if list[i]%2==0:
#         print(f'{list[i]} is an even num')
#         count=count+1 #it just give num of iteration  value 
#     i=i+1
# print(f'no of the evn number are {count}')

# write a program to find even number from list collection and store in new list collection
# list=[23,78,65,89,97]
# newlist=[]
# i=0
# while i<len(list):
#     if list[i]%2==0:
#         newlist=newlist + [list[i]]
#     i=i+1
# print(newlist)

# program sum all digit even num 
# num=96872
# total=0
# while num > 0:
#     digit = num%10
#     total=total+digit
#     num=num//10
# print(f'sum of all digit :{total}')


# write program to find product all digit 
# num=96872
# product=1
# while num > 0:
#     digit=num%10
#     product=product*digit
#     num=num//10
# print(f'product of all digit:{product}')


# write a program even odd total product digit
# num=97845
# even_total=0
# even_product=1
# odd_total=0
# odd_product=1
# while num > 0:
#     digit = num % 10
#     if digit%2==0:
#         even_total=even_total+digit
#         even_product=even_product*digit
#     else:
#         odd_total=odd_total+digit
#         odd_product=odd_product*digit
#     num=num//10
# print(f'sum of even num{even_total}')
# print(f'sum of even digit{even_product}')
# print(f'sum of even num{odd_total}')
# print(f'sum of even digit{odd_product}')


# write a program to reverse a num