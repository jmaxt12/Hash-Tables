# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return f'key: {self.key}, value: {self.value}'


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity 


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = (( hash << 5) + hash) + ord(x)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
 def recursion1(node):
    loop = True
    while loop:
        if node.next != None:
            node = node.next
            recursion1(node)
        else:
            loop = False
            return node


def recursion2(node, key):
    loop = True
    while loop:
        if node.key != key or node.next.next != None:
            prev_node = node
            node = node.next
            recursion2(node, key)
        else:
            loop = False
            return [node, node.next]



def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    insertThis = LinkedPair(key, value)
    bucketRootNode = hash_table.storage[index]
    foo = None

    if bucketRootNode is None:
        hash_table.storage[index] = insertThis
        return True
    else:
        current_node = recursion1(bucketRootNode)

    current_node.next = insertThis

HT = HashTable(10)
hash_table_insert(HT, 'John', "Smith")
print(HT.storage)
print(HT.storage[0])
        

# Get index by hashing key 
# InsertThis = Pair(key, value, None)
# bucketRootNode = hash_table.storage[index]


# Check bucketRootNode and see if its empty
    # If so hash_table.storage[index] = Pair

# If not execute the following:
    # While bucketRootNode.next != None
        # keep going
    # bucketRootNode.next = InsertThis 

 # '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    rootNode = hash_table.storage[index]
    if hash_table.storage[index] == None:
        return None
    else:
        prev_node = recursion2(rootNode, key)[0]
        cur_node = recursion2(rootNode, key)[1]
        
        prev_node.next = cur_node.next
        cur_node = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
 