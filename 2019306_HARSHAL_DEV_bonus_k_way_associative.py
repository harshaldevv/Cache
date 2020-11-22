#cache_size = 16  #cachesize = CacheLines* Blocksize   #int(input("Enter cache size "))
no_of_cache_line = 4 #int(input("Enter the number of cache lines "))
#block_size = 4 #int(input("Enter block size or main memory size "))
#^^^original   neeche wali line is ankit input
block_size = 4 #int(input("Enter block size or main memory size "))
value_of_k = 2


badi_cache = [] # <== iska size CL = 4 
badi_cache_ka_size = no_of_cache_line

choti_cache = [] # <=== iska size CL =2 
choti_cache_ka_size = no_of_cache_line//2

no_of_sets_for_badi_cache = no_of_cache_line//value_of_k

no_of_sets_for_choti_cache = (no_of_cache_line//2)//value_of_k

for i in range(no_of_sets_for_badi_cache):
    badi_cache.append([])

for i in range(no_of_sets_for_choti_cache):
    choti_cache.append([])


def loading(address):
    loading_in_badi_cache(address)
    loading_in_choti_cache(address)


def loading_in_badi_cache(address):
    block_no = int(address)//block_size #integer division
    set_no = block_no%no_of_sets_for_badi_cache #set no is the set no jisme hamara block jayega

    if len(badi_cache[set_no]) >= value_of_k:

        if block_no in badi_cache[set_no]:
            address_index = badi_cache[set_no].index(block_no)
            badi_cache[set_no].pop(address_index)
            badi_cache[set_no].append(block_no)

        else:
            badi_cache[set_no].pop(0)
            badi_cache[set_no].append(block_no)

    else:
        if block_no in badi_cache[set_no]:
            address_index = badi_cache[set_no].index(block_no)    
            badi_cache[set_no].pop(address_index)
            badi_cache[set_no].append(block_no)
            
        else:
            badi_cache[set_no].append(block_no)

    

def loading_in_choti_cache(address):
    block_no = int(address)//block_size #integer division
    set_no = block_no%no_of_sets_for_choti_cache #set no is the set no jisme hamara block jayega

    if len(choti_cache[set_no]) >= value_of_k:

        if block_no in choti_cache[set_no]:
            address_index = choti_cache[set_no].index(block_no)
            choti_cache[set_no].pop(address_index)
            choti_cache[set_no].append(block_no)

        else:
            choti_cache[set_no].pop(0)
            choti_cache[set_no].append(block_no)

    else:
        if block_no in choti_cache[set_no]:
            address_index = choti_cache[set_no].index(block_no)    
            choti_cache[set_no].pop(address_index)
            choti_cache[set_no].append(block_no)
            
        else:
            choti_cache[set_no].append(block_no)
    

def searching(address):
    searching_in_choti_cache(address)

def searching_in_choti_cache(address):
    block_no = int(address)//block_size
    set_no = block_no%no_of_sets_for_choti_cache

    if block_no in choti_cache[set_no]:
        print(str(address) +" is a hit")
#        loading(address)

        address_index = choti_cache[set_no].index(block_no)
        choti_cache[set_no].pop(address_index)
        choti_cache[set_no].append(block_no)

        loading_in_badi_cache(address)

        return


    else:
        searching_in_badi_cache(address)

def searching_in_badi_cache(address):
    block_no = int(address)//block_size
    set_no = block_no%no_of_sets_for_badi_cache

    if block_no in badi_cache[set_no]:
        print(str(address) +" is a hit")
#        loading(address)

        address_index = badi_cache[set_no].index(block_no)
        badi_cache[set_no].pop(address_index)
        badi_cache[set_no].append(block_no)

        loading_in_choti_cache(address)

    else:
        print(str(address) + " is a miss")
        loading(address)


    
searching(1)
print(badi_cache)
print(choti_cache)
print()

searching(0)
print(badi_cache)
print(choti_cache)
print()

loading(0)
print(badi_cache)
print(choti_cache)
print()

loading(5)
print(badi_cache)
print(choti_cache)
print()

loading(11)
print(badi_cache)
print(choti_cache)
print()

loading(6)
print(badi_cache)
print(choti_cache)
print()

loading(8)
print(badi_cache)
print(choti_cache)
print()

loading(1)
print(badi_cache)
print(choti_cache)
print()


loading(8)
print(badi_cache)
print(choti_cache)
print()

searching(5)
print(badi_cache)
print(choti_cache)
print()

searching(1)
print(badi_cache)
print(choti_cache)
print()

searching(5)
print(badi_cache)
print(choti_cache)
print()

loading(5)
print(badi_cache)
print(choti_cache)
print()

#searching()
#print(badi_cache)
#print(choti_cache)


print(badi_cache)
print(choti_cache)
print()