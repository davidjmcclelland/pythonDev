numElements=int(input('how many elements in array? '))
arr=[]
tot = int(0)
avg = float(0.0)
for i in range(0,numElements,1):
	myElement=int(input('Input number: '))
	arr.append(myElement)
print('Your grades: ')
for i in range(0,numElements,1):
	print(arr[i])
	tot = tot + int(arr[i])
avg=tot/numElements
print('your average is: ',avg)
