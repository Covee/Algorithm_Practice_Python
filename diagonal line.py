# 대각선으로 별 출력하기

a = 1

for i in range(5):
	for j in range(a):
		if i == j:
			print("*", end=" ")
		else :
			print(" ", end=" ")
	print()
	a+=1