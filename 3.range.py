# range

nums=range(6)
print(nums)

nums=range(6)
result=list(nums)
print(result)

nums=range(6)
result=tuple(nums)
print(result)

nums=range(6)
result=set(nums)
print(result)

nums=range(6)
result=str(nums)
print(result)


num1=range(1,6)
num2=range(10,51,10)
result={**dict(zip(num1,num2))}
print(result)

nums=range(10,5,-1)
print(list(nums))

nums=range(10,101,10)
result=list(nums)
print(result)
print(result[0])
print(result[-1])
print(result[5])
print(result[4])
# print(result[13])  #index error

r=range(1,11)
# [1,2,3,4,5,6,7,8,9,10]
print(list(r))

print(list(r[1:5:]))
print(list(r[2:8:]))
print(list(r[:5:]))
print(list(r[5::]))
print(list(r[1:9:2]))

# negative slicing
r=range(1,11)
# [1,2,3,4,5,6,7,8,9,10]
print(list(r))

print(list(r[8:2:-1]))
print(list(r[9:3:-1]))
print(list(r[7:1:-2]))
print(list(r[9:4:-2]))
print(list(r[5:0:-1]))



# reverse slicing
r=range(1,11)
# [1,2,3,4,5,6,7,8,9,10]
print(list(r))

print(list(r[::-1]))
print(list(r[::-2]))
print(list(r[8::-2]))
print(list(r[6:1:-2]))
print(list(r[9:2:-2]))

# eval function
num=eval(input('enter the value:'))
print(type(num))

# write program tod display emp num and emp sal
empno=eval(input("enter the emp no"))
ename=input('enter the employee name:')
salary=eval(input('enter the salary'))

print('\n employee details')
print(f'employee number is: {empno}')
print(f'employee ename is: {ename}')
print(f'employee salary is: {salary}')