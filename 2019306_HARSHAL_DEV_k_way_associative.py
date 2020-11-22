cache_size = 16 #int(input("Enter cache size "))
no_of_cache_line = 4 #int(input("Enter the number of cache lines "))
block_size = 4 #int(input("Enter block size or main memory size "))
value_of_k = 2 #int(input("Enter the value of K "))


cache = [] 

main_memory = []

no_of_sets = no_of_cache_line//value_of_k

for i in range(no_of_sets):
    cache.append([])

def loading(address):
    block_no = int(address)//block_size #integer division
    set_no = block_no%no_of_sets #set no is the set no jisme hamara block jayega

    if len(cache[set_no]) >= value_of_k:

        if block_no in cache[set_no]:
            address_index = cache[set_no].index(block_no)
            cache[set_no].pop(address_index)
            cache[set_no].append(block_no)

        else:
            cache[set_no].pop(0)
            cache[set_no].append(block_no)

    else:
        if block_no in cache[set_no]:
            address_index = cache[set_no].index(block_no)    
            cache[set_no].pop(address_index)
            cache[set_no].append(block_no)
            
        else:
            cache[set_no].append(block_no)

def searching(address):
    block_no = int(address)//block_size
    set_no = block_no%no_of_sets

    if block_no in cache[set_no]:
        print(str(address) +" is a hit")
#        loading(address)

        address_index = cache[set_no].index(block_no)
        cache[set_no].pop(address_index)
        cache[set_no].append(block_no)

    else:
        print(str(address) + " is a miss")
        loading(address)

loading(0)
print(cache)
loading(1)
print(cache)
loading(4)
print(cache)
loading(8)
print(cache)
loading(12)
print(cache)
searching(3)
print(cache)
searching(16)
print(cache)
searching(17)
print(cache)
searching(2)
print(cache)
searching(21)
print(cache)
searching(12)
print(cache)

print()
print()
print("final cache")
print(cache)