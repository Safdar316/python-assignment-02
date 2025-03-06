# 4..  ASSIGNMENT OPERATOR
#  1) ---(=) this operator is used to assign a value in variable
a = 2
print(a) #  a = 2

#  2) --- (+=) this operator is used to add a value in variable

a += 5   
print(a) #  a = a + 5, a = 2 + 5 = 7, a = 7    

#  3) --- (-=) this operator is used to subtract a value in variable
a -= 3  # a = a - 3 
print(a)  #  a = a - 3, a = 7 - 3 = 4, a = 4

#  4) --- (*=) this operator is used to multiply a value in variable

a *= 5  #  a = a * 5
print(a)  #  a = a * 5, a = 4 * 5 = 20 , a = 20
 
#  5) --- (/=) this operator is used to divide a value in variable
a /= 5 #  a = a / 5
print(a)  #  a = a / 5, a = 20 / 5 = 4

#  6) --- (//=) this operator is used to divide a value in variable

a //= 3  # a = a // 3 
print(a) #  a = a // 3, a = 4 // 3 = 1


# IDENTITY OPERATORS
# 1) --  is operator
x = 3
y = x
print(x is y) # True

# 2) --- is not operator

v = 45
m = 89
f = m is not v
f = m is not f


#  MEMBERSHIP OPERATORS
#  1) -- in

friends = ["Safdar", "Zafar","Asif","Adil"]
print("Safdar" in friends)
print("hameed" not in friends)

#  2) --- not in

name = "safdar"
print("safdar" not in name) # False
print("S" not in name) # True

#  BITWISE NOT (~) OPERATOR

num_val = 23
result = ~num_val
print(result) # result = -(num_val + 1), result = -(23 + 1), result = -24
