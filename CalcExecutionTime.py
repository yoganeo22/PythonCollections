# Import time module
import time
import threading

# record start time
start = time.time()

# define a sample code segment | Program code
a = 0
for i in range(1000):
	a += (i**100)
time.sleep(1)

# record end time
end = time.time()

# print the difference between start and end time in milli. secs
print("The time of execution of above program is :",
	(end-start) * 10**3, "ms")

# output: - The time of execution of above program is : 1001.8775463104248 ms
