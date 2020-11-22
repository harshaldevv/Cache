cache_size = 16 #int(input("Enter cache size "))
no_of_cache_line = 4 #int(input("Enter the number of cache lines "))
block_size = 4 #int(input("Enter block size or main memory size "))


cache = [] 

main_memory = []

def loading(address): 
	#address ke corresponging block no and line number (addres = "WORD") 0
	block_no = int(address)//block_size #integer division
	line_no = block_no % no_of_cache_line #integer division

	#tuple bana dia line no and block no  and append in cache

	if (len(cache)==0):
		cache.append((line_no,block_no))

	temp_line_block = (line_no,block_no)



	temp_counter = -5
	mera_i = -5
	for i in range(len(cache)):
		if cache[i][0] == line_no:
			temp_counter+=10
			mera_i = i
			break


	if (temp_line_block in cache):
		pass
	elif (temp_counter >0):
		cache[mera_i] = temp_line_block
	else:
		cache.append(temp_line_block)

#	else:
#		for i in range(len(cache)):
#			if cache[i][0] == line_no:
#				temp_counter+=10
#				cache[i] = temp_line_block
#				break
		


def searching(address):
	block_no = int(address)//block_size #integer division
    line_no = block_no % no_of_cache_line #integer division
    
    temp_line_block = (line_no,block_no)
    if temp_line_block in cache:
        print(str(address) +" is a hit")
    else:
    	print(str(address) + " is a miss")
    	loading(address)



loading(17)
loading(5)
print(cache)

searching(3)  #repalces 17 as 3 =(0,0) and 17 = (0,4)  #yes ab ho gaya replace
print(cache)

loading(5)
print(cache)

searching(17)
print(cache)

