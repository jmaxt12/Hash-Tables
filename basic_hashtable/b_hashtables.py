

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum size the array can be
        self.count = 0  # Current size being used
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
#     Notes from Stack overflow 
            # hash(unsigned char *str)
            # {
            #     unsigned long hash = 5381;
            #     int c;

            #     while (c = *str++)
            #         hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

            #     return hash;
            # }
    hash = 5381
    for i in string:
        hash = ((hash << 5) + hash) + ord(i)

    return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):

    hashed_index = hash(key, hash_table.capacity)
    pair = Pair(key, value)
    stored_pair = hash_table.storage[hashed_index]

    if hash_table.storage[hashed_index] is not None:
    	print(f'Overwriting key {hash_table.storage[hashed_index][0]} with {key}!')

    hash_table.storage[hashed_index] = (key, value)

    return


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashed_index = hash(key, hash_table.capacity)

    if not hash_table.storage[hashed_index]:
    	return print(f'Key {key} not found!')

    hash_table.storage[hashed_index] = None

    return


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hashed_index = hash(key, hash_table.capacity)

    retrieved = hash_table.storage[hashed_index]

    if retrieved:
    	return retrieved[1]
    else:
    	return retrieved


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
