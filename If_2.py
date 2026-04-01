li=eval(input())
print(li)
li_1=li[2::2]
print(li_1)
a=li_1[0]
b=li_1[1]
c=li_1[2]
d=li_1[3]
print(a,b,c,d)
if a>b and a>c and a>d :
	print("a is bigger")
elif b>c and b>d :
	print("b is bigger")
elif  c>d :
	print("c is bigger")
else :
	print("d is bigger")


