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
    line_no = block_no % badi_cache_ka_size #integer division

    if (len(badi_cache)==0):
        badi_cache.append((line_no,block_no))

    temp_line_block = (line_no,block_no)



    temp_counter = -5
    mera_i = -5
    for i in range(len(badi_cache)):
        if badi_cache[i][0] == line_no:
            temp_counter+=10
            mera_i = i
            break


    if (temp_line_block in badi_cache):
        pass
    elif (temp_counter >0):
        badi_cache[mera_i] = temp_line_block
    else:
        badi_cache.append(temp_line_block)


def loading_in_choti_cache(address):
    block_no = int(address)//block_size #integer division
    line_no = block_no % choti_cache_ka_size #integer division

    if (len(choti_cache)==0):
        choti_cache.append((line_no,block_no))

    temp_line_block = (line_no,block_no)



    temp_counter = -5
    mera_i = -5
    for i in range(len(choti_cache)):
        if choti_cache[i][0] == line_no:
            temp_counter+=10
            mera_i = i
            break


    if (temp_line_block in choti_cache):
        pass
    elif (temp_counter >0):
        choti_cache[mera_i] = temp_line_block
    else:
        choti_cache.append(temp_line_block)






def searching_in_choti_cache(address):
    block_no = int(address)//block_size #integer division
    line_no = block_no % choti_cache_ka_size #integer division
    temp_line_block = (line_no,block_no)

    if temp_line_block in choti_cache:
        print(str(address) +" is a hit")
        return

    else:
        searching_in_badi_cache(address)

def searching_in_badi_cache(address):
    block_no = int(address)//block_size #integer division
    line_no = block_no % badi_cache_ka_size #integer division
    temp_line_block = (line_no,block_no)

    if temp_line_block in badi_cache:
        print(str(address) +" is a hit")
        loading_in_choti_cache(address)
        return

    else:
        print(str(address) + " is a miss")
        loading(address)
       


def searching(address):
    searching_in_choti_cache(address)
    #pseudo code:
    # if found in choti cache
    #    print(hit) and exit
    #else:
    #    PANIC :O ;_;

searching(4)
print(badi_cache)
print(choti_cache)
searching(5)

print()
print(badi_cache)
print(choti_cache)
searching(6)


print()
print(badi_cache)
print(choti_cache)

searching(7)


print()
print(badi_cache)
print(choti_cache)

loading(0)

print()
print(badi_cache)
print(choti_cache)

loading(1)

print()
print(badi_cache)
print(choti_cache)

loading(2)

print()
print(badi_cache)
print(choti_cache)

loading(3)

print()
print(badi_cache)
print(choti_cache)

searching(3)

print()
print(badi_cache)
print(choti_cache)

searching(1)

print()
print(badi_cache)
print(choti_cache)
