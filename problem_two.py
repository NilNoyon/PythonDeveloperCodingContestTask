# Left Rotate Method..
def leftRotate(arr, d):
	return [arr[(i + d) % len(arr)] 
               for i, x in enumerate(arr)]
#function to print an array  
def printArray(arr, size): 
    for i in range(size): 
        print ("%d" % arr[i], end=" ") 


# Main Code..
print('Insert the array size and the number of rotation you want:')
n = int(input())
d = int(input())

if n >= 1 and n <= 100000 and d >= 1 and d <= n:
	a = list(int(num) for num in input("Enter the list numbers separated by space: ").strip().split())[:n]
	print("New List: ", a)
	b = leftRotate(a,d)
	print("rotated List: ", b)
else:
	print('You have enter wrong data for number rotation')
