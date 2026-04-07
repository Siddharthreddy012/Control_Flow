s=[(1,2,3,4),(4,3,2,1),(1,2,3,4)]
for x in s :
	for y in x: 
		print(y,end=" ")
	print( )
print("-----------------------")			
i=2
for row in range(5) :
	for col in range(4) :
		if row % 2 == 0 :
			print(i,end=" ")
			i +=2
		else :
			i -= 2
			print(i,end= " ")
			
	print( )

print("-----------------")

s=eval(input())
row, col = s
print(row)
print(col)
for row in range(s[0]) :
	for col in range(s[1]):
		print("*",end=" ")
	print( )

print("-------------------")

i=[1,4,3,2,1]
n=-1
for x in i:
	print(i[n])
	n-=1
	 
print("------------------------")

d=((1,2,3,4),(6,7,8,9),[1,2,3,4],[4,5,6,7])
temp=0
for x in d :
	if temp % 2 ==0 :
		for y in  range(-1,-len(x)-1,-1):	
				print(x[y],end=" ")
		
	else : 
		for y in x :
				print(y,end=" ")

	temp += 1		
		
	print( )