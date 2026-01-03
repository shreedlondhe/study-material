# link for question
# https://techpluslifestyle.com/technology/python-interview-programs/#:~:text=Python%20Interview%20Programs.%201%20%231.%20Prime%20Number%20Program,sorting%20in%20descending%20order%20based%20on%20values.%20



# check no is prime or nt*********************************************
#
# a = int(input('enter a number you want to check prime or not'))
# count = 0
# for i in range(2,a+1):
#     if(a%i == 0):
#         count=count+1
#
#
# if count == 1:
#     print("number is prime")
# else:
#     print("number is not a prime")

##########################################################################################
# check the number is even or odd
# num = int(input("enter a numeber to check it is even or odd"))
# if num % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

#############################################################################################
# to print ip address and hostname(computer name)

# import socket
# # to print hostname
# hostname = socket.gethostname()
#
# # to print ip address
# IPADD= socket.gethostbyname(hostname)
#
# print(IPADD)

#################################################################################################
# listcomprehension

# list_even = [i for i in range(1,20) if i%2==0]
#
# print(list_even)

###################################################################################################
#listcomprihension for odd no
#
# list_odd = [i for i in range(1,30) if i%2!=0]
#
# print(list_odd)

#########################################################################################################
# # compare to list and return the common recod from both the list
# a = [1, 1, 2, 3, 5, 8, 13, 30, 55]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 13]
#
# # common record from both table i.e itersect
# print(set(a) & set(b))
#
# # to print unic record in both the list
# print(set(a) | set(b))

#################################################################################################
# to print unic record in both the list
# a = [1, 1, 2, 3, 5, 8, 13, 30, 55]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 13]
#
# c = a+b
# print(c)
# d = set(c)
# print(d)
###################################################################################################

# # reversed the list without using inbuild function
# a = [10,50,3,60,90,70,60,20]
# # b = a[::-1]
# # print(b)
#
# # method
# a.reverse()
# print(a)


###################################################################################################
# # revers string in python
# name  = "mayur"
# b = name[::-1]
# print(b)

# method - 2
# name  = "mayur"
# l = len(name)
# for a in range(l-1,-1,-1):
#     print(name[a])

###################################################################################################
# check number is palidrome or not

# a = '121'
# b = a[::-1]
# if a==b:
#     print("number is palidromwe")

# check string is palidrom or not
# name1 = 'nitin'
# name2 = name1[::-1]
# if name1==name2:
#     print("name is polidrome")

##################################################################################################
# find largest no in list

# def minimum(a):
#     min = a[0]
#     for i in a:
#         if i < min:
#             min = i
#     return min
# def maximum(a):
#     max = a[0]
#     for i in a:
#         if i > max:
#             max = i
#     return max
# mylist = [12,45,78,60,98,95]
# min = minimum(mylist)
# print(min)
# max = maximum(mylist)
# print(max)

##################################################################################################################
# swap two number without using 3rd number
# a = 10
# b = 20
# print("a=",a,"b=",b)
# a,b = b,a
# print("a=",a,"b=",b)

##########################################################################
# print the addition of digit
# a = (input())
# b = 0
# for i in a:
#     b = b + int(i)
#
# print(b)

#####################################################################################################


















