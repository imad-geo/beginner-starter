############## Exercise 01
# x = 10 
# y = 20 
# x , y = y ,x
# print (x , y)
# if x > y :
#     print (f" {x} is greater than {y}")
# if x < y :
#     print (f" {x} is smaler than {y}")
# if x == y :
#     print (f" {x} is equal than {y}")


################# Exercise 02

# def operation (n1, n2):
#     for i in range (1,6):
#         i = int(input("give me number between 1 to 5 \n witch mean (1:+),(2:-),(3:*),(4:/),(5:exit) : "))
#         if i == 1 :
#             s = n1 + n2
#         if i == 2 :
#             s = n1 - n2
#         if i == 3 : 
#             s = n1 * n2
#         if i == 4 :
#             s = n1 / n2
#         if i == 5:
#             return print ("exit")
#         if i ==0 or i > 5 :
#             print ("error")
#             return operation ( n1, n2 )
#         return s
        
# num1 = 5
# num2 = 3
# print (operation(num1, num2))

################### Exercise 03

# tepm = 60
# print ( """ 1:convert celsius to Fahrenheit\n 2:convert celsius to kelvin \n 3: to exit """)


# def tmp_converter(temp):
#     i = int(input(" choose a number : 1 , 2, or 3: "))
#     if i == 1 :
#         k = temp + 273.15
#         print (f"the temperature in kelvin is {k}")
#     if i == 2 :
#         k = (temp * 9 / 5)+ 32
#         print (f"the temperature in Fehrenhait is {k}")
#     if i == 3:
#         return print ("exit")
#     return k 


# print (tmp_converter(10))

################ Exercise 04

# number = int(input("please, give me a number , we will check if this number is odd oe even: "))
# if number % 2 == 0:
#     print (f"this number {number} is even")
# else:
#     print (f"this number {number} is odd")

################ Exercise 05

# capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# smallalphabets="abcdefghijklmnopqrstuvwxyz"
# digits="0123456789"
# password = input ("your password please : ") #paPa2020
# a , b , c = 0 ,0 , 0
# if len(password)< 8:
#     print ("password is weak")
# else:
#     for i in password:
#         if i in capitalalphabets:
#             a += 1
#         if i in smallalphabets:
#             b += 1
#         if i in digits : 
#             c += 1
#     # print (a, b ,c)
#     if a >= 1 and b >= 1 and c >= 1 :
#         print ( " good password")
#     else:
#         print ("invalid password")
        
        
###################


    
               
    

