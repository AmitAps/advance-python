import time 

start = time.time()
for i in range(20):
	print(i)
	time.sleep(1) #Sleep for 1 second

end = time.time()

print(f"Time needed to excuted this code is {end - start} seconds!")
