def merge(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		merge(L)
		merge(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

if __name__ == '__main__':
	arr = [15,69,20,13,5,19]
	print("Given array is", end="\n")
	print(*arr)
	merge(arr)
	print("Sorted array is: ", end="\n")
	print(*arr)

