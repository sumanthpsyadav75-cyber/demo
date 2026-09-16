# num=47
# if num % 2 == 0:
#     print(f'{num} is an even number')
# elif num % 2 !=0:
#     print(f'{num} is an odd number')

# write a program largest value among 3 number
# a,b,c=50,80,30
# if a>b and a>c:
    # print(f'{a} is an greatest number')
# elif b>a and b>c:
    # print(f'{b} is an greatest number')
# elif c>a and c>b:
    # print(f'{c} is an greatest number')
# 
# write a program to find first smallest number among 4 number
# a,b,c,d 50,30,70,30
# if a<b and a<c and a<d:
#     print(f'{a} is the smallest number')
# elif b<c and b<a and b<d:
#     print(f'{b} is the smallest number')
# elif c<a and c<b and c<d:
#     print(f'{b} is the smallest number')
# elif d<a and d<b and d<c:
#     print(f'{b} is the smallest number')


# //write a program to check given character is uppercase , lowercase ,digit or special symbol

# char=input("enter the object")
# if char >='a' and char <='z':
#     print(f'{char} it is a lowercase')
# elif char >= 'A' and char <='Z':
#     print(f'{char} it is uppercase')
# elif char >= '0' and char <='99999':
#     print(f'{char} it is digit')
# elif not((char >='a' and char <='z') or (char >='A' and char <='Z') 
#  or (char >='0' and char <='99999'))
# else:
#     print(f'{char} it is special symbol')
    
# write a program to check first character of given string is uppercase, lowecase,digit,special sym+++bol

# string='python'
# string=str[0]
# if char >='a' and char <='z':
#     print(f'{char} it is a lowercase')
# elif char >= 'A' and char <='Z':
#     print(f'{char} it is uppercase')
# elif char >= '0' and char <='99999':
#     print(f'{char} it is digit')
# elif not((char >='a' and char <='z') or (char >='A' and char <='Z') 
#  or (char >='0' and char <='99999'))
# else:
#     print(f'{char} it is special symbol')
    
# other way

# string='python'
# if char[0] >='a' and char[0]<='z':
#     print(f'{char} it is a lowercase')
# elif char [0]>= 'A' and char [0]<='Z':
#     print(f'{char} it is uppercase')
# elif char [0]>= '0' and char [0]<='99999':
#     print(f'{char} it is digit')
# elif not((char [0]>='a' and char [0]<='z') or (char [0]>='A' and char [0]<='Z') 
#  or (char [0]>='0' and char[0] <='99999'))
# else:
#     print(f'{char} it is special symbol')

\
# write a program to perform atm transaction [checkbalance ,deposit ,withdrawn]
# balance=99999
# print('1.deposit money')
# print('2.check balance')
# print('1.withdrawn money')

# choice=int(input('enter the number 1/2/3'))
# if choice==1:
#     deposit=float(input('enter the amount to deposit:'))
#     balance=balance+deposit
#     print(f'{deposit}has been deposited')
#     print(f'after deposit updated balance:{balance}')

# elif choice==2:
#     print(f'updated balance is :{balance}')
# elif choice ==3:
#     choice=float(input('enter the amt to withdrawn'))
#     balance=balance-withdrawn
#     print(f'{withdrawn} has been debited')
#     print(f'after withdrawn updated balance : {balance}}')