# multi value datatype

# string//it is imutable
# string=str()
# print(string);

# string='hello python'
# print(string);
# print(type(string));

# slicing
# s1='education'
# print(s1[-9::3]);
# print(s1[-9:3:3]);
# print(s1[-8:5:2]);
# print(s1[ ::-1]);
# print(s1[-9::]);

#list //it is a mutable
# [1,2,3.4,5] homogenous element that has same datatype value
# [1,2,true,"smith",3.4,'false',5] homogenous element that has hold  different datatype value

# index into list
# list=[10,30,50,"smith",True]
# print(list[3])
# print(list[2])
# print(list[0])
# print(list[1])

# list nested
# list=[10,30,50,(2,7,8),"smith",True]
# print(list[2])
# print(list[3][0])
# print(list[4][0])
# print(list[3][1])
# print(list[3][2])
# print(list[5][1])

# list update
# list=[10,30,50,(2,7,8),"smith",True]
# list[1]=32
# print(list);
# list=[10,30,50,(2,7,8),"smith",True]
# list[2]=32
# print(list);


# list delete
# list=[10,30,50,(2,7,8),"smith",True]
# del list[1]
# print(list);
# del list[3]
# print(list);

# list positive  [start:value,stop:value,step:value]
# list=[10,"python",3.14,True,[1,2],{"a":1},{5,6}]
# print(list[1:7:2]);
# print(list[5:6:1]);
# print(list[4:6:1]);
# print(list[2:7:2]);
# print(list[0:6:2]);
# print(list[6:6:2]);
# print(list[7:7:7]);


# list negative  [start:value,stop:value,step:value]
# list=[10,"python",3.14,True,[1,2],{"a":1},{5,6}]
# print(list[-7:7:2]);
# print(list[-5:6:1]);
# print(list[-4:6:1]);
# print(list[-3:6:1]);
# print(list[-7:2:2]);
# print(list[-5:5:5]);


# tuple//it immutable 
# t=(10,20,30,"smith",True,78,90,23)
# print(t);
# print(t[1:3:1]);
# print(t[4:6:]);
# print(t[-1:-3:1]);
# print(t[-1:6:-1]);
# print(t[6:-3:2]);


# set//ot mutable  it access index value
# set={98,10,20,30,70,56,10}
# print(set);
# print(set);

# set={98,[10,20,30,70],56,10}
# print(set);we cant acces we want to type casting 

# dictionary
# write program display help of keys 

# data={'ename':'sumanth',
#       'salary':50000
#       }
# print(data);
# print(type(data));


# write program to display ductionary to collection
# data={'ename':'sneha',
#       'salary':20000
#       }
# print(data.keys());
# print(data.values());
# print(data.items())

# emp={
#     'emp1':['smith',70000,'analyst'],
#     'emp2':['ram',40000,'accounting'],
#     'emp3':['varun',50000,'manager']
# }
# print(emp)
# print(emp.keys());
# print(emp.values());
# print(emp.items());
