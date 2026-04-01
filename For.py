a = [1,10,15,20,45,65,42,-12,-12.2,-12.15,10.25]
for x in a :
	if x % 2 == 0 :
 			print(x)
b=[4,9,16,25,72,81,100]
for x in b:
	print((x)**0.5)

for x in range(0,9,-1) : 
	print(x)

c=int(input())
k=0
for x in range(1,c+1,1) :
	if c % x ==0 :
		k += 1
if k==2 :
	print("Prime")
else :
	print("Not prime")