def square(z):
	print(z,"的平方是",z*z)


x = int(input("請輸入一個正整數："))
print("您輸入的是,x")

if(x<0):
	print("請輸入的值為負數")
else(x==0):
	print("您輸入的值小於等於0")
else:
	for i in range(1,x+1):
		square(i)
