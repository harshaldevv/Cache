cache_size = 16  #cachesize = CacheLines* Blocksize   #int(input("Enter cache size "))
no_of_cache_line = 4 #int(input("Enter the number of cache lines "))
#block_size = 4 #int(input("Enter block size or main memory size "))
#^^^original   neeche wali line is ankit input
block_size = 1 #int(input("Enter block size or main memory size "))


badi_cache = [] # <== iska size CL = 4 
badi_cache_ka_size = no_of_cache_line

choti_cache = [] # <=== iska size CL =2 
choti_cache_ka_size = no_of_cache_line//2

def loading(address):
    loading_in_badi_cache(address)
    loading_in_choti_cache(address)


def loading_in_badi_cache(address):
    block_no = int(address)//block_size #integer division

    if len(badi_cache) >= badi_cache_ka_size:
        if block_no in badi_cache:
        #    now doing loading of the hit address
   # aka additional_loading(address)
            address_index = badi_cache.index(address)
            badi_cache.pop(address_index)
            badi_cache.append(address)
            
        else:
            badi_cache.pop(0)
            badi_cache.append(block_no)
        
    else:
        if block_no in badi_cache:
            address_index = badi_cache.index(address)
            badi_cache.pop(address_index)
            badi_cache.append(address)
              #check this block 
        else:
            badi_cache.append(block_no)


def loading_in_choti_cache(address):
    block_no = int(address)//block_size #integer division

    if len(choti_cache) >= choti_cache_ka_size:
        if block_no in choti_cache:
        #    now doing loading of the hit address
   # aka additional_loading(address)
            address_index = choti_cache.index(address)
            choti_cache.pop(address_index)
            choti_cache.append(address)
            
        else:
            choti_cache.pop(0)
            choti_cache.append(block_no)
        
    else:
        if block_no in choti_cache:
            address_index = choti_cache.index(address)
            choti_cache.pop(address_index)
            choti_cache.append(address)
              #check this block 
        else:
            choti_cache.append(block_no)


def searching_in_choti_cache(address):
    block_no = int(address)//block_size #integer division

    if block_no in choti_cache:
        print(str(address) + " is a hit")

        #now doing loading of the hit address
   # aka additional_loading(address)

   

        address_index = choti_cache.index(address)
        choti_cache.pop(address_index)
        choti_cache.append(address)
        
        loading_in_badi_cache(address)

        return 

    else:
        searching_in_badi_cache(address)



def searching_in_badi_cache(address):
    block_no = int(address)//block_size #integer division

    if block_no in badi_cache:
        print(str(address) + " is a hit")

        #now doing loading of the hit address
   # aka additional_loading(address)

   

        address_index = badi_cache.index(address)
        badi_cache.pop(address_index)
        badi_cache.append(address)

        loading_in_choti_cache(address)

    else:
        print(str(address) + " is a miss")
        loading(address)



def searching(address):
    searching_in_choti_cache(address)



searching(4)
print(badi_cache)
print(choti_cache)

searching(5)
print(badi_cache)
print(choti_cache)

searching(6)
print(badi_cache)
print(choti_cache)

searching(7)
print(badi_cache)
print(choti_cache)

loading(0)
print(badi_cache)
print(choti_cache)

loading(1)
print(badi_cache)
print(choti_cache)

loading(2)
print(badi_cache)
print(choti_cache)

loading(3)
print(badi_cache)
print(choti_cache)

searching(3)
print(badi_cache)
print(choti_cache)

searching(1)
print(badi_cache)
print(choti_cache)

searching(3)
print(badi_cache)
print(choti_cache)