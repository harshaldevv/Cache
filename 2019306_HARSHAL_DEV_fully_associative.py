#cache_size = 16 #int(input("Enter cache size "))
#no_of_cache_line = 4 #int(input("Enter the number of cache lines "))
#block_size = 4 #int(input("Enter block size or main memory size "))


#basically cache size = no_of_Cache lines x block_size
cache_size = 4 #int(input("Enter cache size "))
no_of_cache_line = 4 #int(input("Enter the number of cache lines "))
block_size = 1 #int(input("Enter block size or main memory size "))


cache = [] 

main_memory = []




def loading(address):
    block_no = int(address)//block_size #integer division

    if len(cache) >= cache_size:
        if block_no in cache:
        #	now doing loading of the hit address
   # aka additional_loading(address)
        	address_index = cache.index(address)
        	cache.pop(address_index)
        	cache.append(address)
            
        else:
            cache.pop(0)
            cache.append(block_no)
        
    else:
        if block_no in cache:
            address_index = cache.index(address)
            cache.pop(address_index)
            cache.append(address)
              #check this block  <= take help from ankit by checking in python tutor
              
        else:
            cache.append(block_no)


def searching(address):    
    block_no = int(address)//block_size #integer division

    if block_no in cache:
        print(str(address) + " is a hit")

        #now doing loading of the hit address
   # aka additional_loading(address)

        address_index = cache.index(address)
        cache.pop(address_index)
        cache.append(address)

    else:
        print(str(address) + " is a miss")
        loading(address)
        


searching(1)
print(cache)
searching(0)
print(cache)
loading(0)
print(cache)
loading(5)
print(cache)
loading(11)
print(cache)
loading(6)
print(cache)
loading(8)
print(cache)
loading(1)
print(cache)
loading(8)
print(cache)
searching(5)
print(cache)
searching(1)
print(cache)

