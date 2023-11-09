# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
def partition(array, low, high):

	# choose the rightmost element as pivot
	pivot = array[high]

	# pointer for greater element
	i = low - 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])
			#print("(array[i], array[j])): ", array[i], " and ", array[j])

	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	#print("(array[i + 1], array[high]): ", (array[i + 1], " and ", array[high]))

	#print("pivot return: ", i+1)
	# Return the position from where partition is done
	return i + 1

# function to perform quicksort
def quickSort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pivot = partition(array, low, high)

		# Recursive call on the left of pivot
		quickSort(array, low, pivot - 1)

		# Recursive call on the right of pivot
		quickSort(array, pivot + 1, high)

if __name__ == "__main__":
	data = [1, 7, 4, 1, 10, 9, -2]
	print("Unsorted Array")
	print(data)

	# Unsorted Array
	# [1, 7, 4, 1, 10, 9, -2]

	size = len(data)

	quickSort(data, 0, size-1)
	#data.sort()

	print('Sorted Array in Ascending Order:')
	print(data)

	# Sorted Array in Ascending Order:
	# [-2, 1, 1, 4, 7, 9, 10]


	# workflow:
	# if low < high	
	#	check pivot
	# 		pivot is at arr[high], and compare with arr[low]
	# 		if pivot higher, then swap values on those index
	#		return pivot value
	#	recursive
	