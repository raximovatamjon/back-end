# inputdagi stringni number holatga o'tkazish print(int(a) + int(b)) mana bunaqa bo'ladi

#1-misol
# a = input("1soni kiriting>>> ")
# b = input("2soni kiriting>>> ")

# print(int(a) + int(b))
# print(float(a) + float(b))    #float oddiy soni butun qiladi mas 3 bo'lsa 3.0 qiladi

#2-misol
# a = input("1soni kiriting>>> ")
# b = input("2soni kiriting>>> ")

# print(int(a) - int(b))
# print(float(a) - float(b))

#3-misol
# a = input("1soni kiriting>>> ")
# b = input("2soni kiriting>>> ")

# print(int(a) * int(b))
# print(float(a) * float(b))

#4-misol
# a = input("1soni kiriting>>> ")
# b = input("2soni kiriting>>> ")

# print(int(a) / int(b))
# print(float(a) / float(b))

#5-misol bu misolda typeni aniqladik
# a =5
# print(type(a))
# b= 6.6
# print(type(b))
# c = "sihihi"
# print(type(c))

#amaloyot qismi

#1-misol
# a =input("Kavadrat tomonini kiriting >>>")
# p =int(a)*4
# print("peremetiri",p)

#2-misol
# a=input("Kvadratni tomonini kirit>>>")
# s=int(a)**2
# print(s)

#3-misol
# a =input("kv tomonlarni bering1>>>")
# b=input("kv ikkinchi tomoni bering2>>>")
# s=int(a)*int(b)
# p=2*int(a)+int(b)
# print(s,p)

#4-misol
# d=int(input("diyametni kiriting>>"))
# p=3.14
# l=p*d
# print(l)

#5-misol
# a=int(input("a soni ni qo'lda kiriting >>>"))
# v=a**3
# s=6*a**2
# print(v, s)

#6-misol
# a=int(input("a soni ni qo'lda kiriting >>>"))
# b=int(input("b soni ni qo'lda kiriting >>>"))
# c=int(input("c soni ni qo'lda kiriting >>>"))
# v=a*b*c
# s=2*(a*b+b*c+a*c)
# print(v,s)

#7-misol
# r=int(input("r soni ni qo'lda kiriting >>>"))
# p=3.14
# l=2*p*r
# s=p*r**2
# print(l,s)

#8-misol
# a=int(input("a soni ni qo'lda kiriting >>>"))
# b=int(input("b soni ni qo'lda kiriting >>>"))
# c=(a+b)/2
# print(c)

#9-misol
# a=int(input("a soni ni qo'lda kiriting >>>"))
# b=int(input("b soni ni qo'lda kiriting >>>"))
# v=(a*b)**0.5
# print(v)

# 10-misol
# a=int(input("a soni ni qo'lda kiriting >>>"))
# b=int(input("b soni ni qo'lda kiriting >>>"))
# print("Ularning yig'indisi", a+b, a*b, a-b, a/b )

#12-misol
# a = int(input("a soni ni qo'lda kiriting >>>"))
# b = int(input("b soni ni qo'lda kiriting >>>"))
# c = (a**2+b**2)**0.5
# p = a + b + c
# print(c,p)

#13-misol
# r1= int(input("r1 soni ni qo'lda kiriting >>>"))
# r2 = int(input("r2 soni ni qo'lda kiriting >>>"))
# p=3.14
# s=p*r1
# s2 = p*r2
# s3 = p*(r1-r2)
# j=(r1>r2)
# print(s,s2,s3,j)

#14-misol
# l = int(input("l soni ni qo'lda kiriting >>>"))
# r = int(input("radisni soni ni qo'lda kiriting >>>"))
# p = 3.14
# L = 2 * p * r
# s =p * r**2
# print(L,s)

#15-misol
# s = int(input("s soni ni qo'lda kiriting >>>"))
# r = int(input("a soni ni qo'lda kiriting >>>"))
# p = 3.14
# L = 2*p*r
# S = p*r**2
# print(L,S)

#17-misol
# a = int(input("a soni ni qo'lda kiriting >>>"))
# b = int(input("b soni ni qo'lda kiriting >>>"))
# c = int(input("c soni ni qo'lda kiriting >>>"))
# print("Ularning yig'indisi", a+c, a*c, a-c, a/c,)
# print("Ularning yig'indisi", b+c, b*c, b-c, b/c )

#25-misol
# x = int(input("x soni ni qo'lda kiriting >>>"))
# y = 3*x**6-6*x**2-7
# print(y)

#26-misol
# x = int(input("x soni ni qo'lda kiriting >>>"))
# y = 4*(x-3)**6-7*(x-3)**3+2
# print(y)

#27-misol
# a = int(input("a soni ni qo'lda kiriting >>>"))
# print(a**2, a**4, a**8)

#28-misol
# a = int(input("a soni ni qo'lda kiriting >>>"))
# print(a**2, a**3, a**5, a**10, a**15)

#31-misol
# Tf = int(input("Tf soni ni qo'lda kiriting >>>"))
# Tc =(Tf-32)*5/9
# print(Tc)

#32-MISOL
# Tf = int(input("Tf soni ni qo'lda kiriting >>>"))
# Tc =(Tf-32)*5/9
# print(Tc)


#33-misol
# a = float(input("konfet narxini kiriting >>>"))
# x = float(input("konfet qancha olishizni kiriting >>>"))
# b = a*x
# print(f"bir kg konfet", a,"so'm", "sizdan",b,"so'm")


#34-MISOL
# a = float(input("shoklood narxini kiriting >>>"))
# x = float(input("shokold qancha olishizni kiriting >>>"))
# javob_shokolod =a*x

# b = float(input("konfet narxini kiriting >>>"))
# y = float(input("konfet qancha olishizni kiriting >>>"))
# javob_konfet = b*y
# javob_oxirgi = javob_shokolod + javob_konfet
# print(f"bir kg konfet", a,"so'm",'turadi',"bir kg shokolod", b,"so'm",'turadi',)
# print(f"Javobi siz shokolod", x,"kg oldiz", "konfet", y, "kg oldiz", "ikkalasini narxi", javob_oxirgi,"so'm")
