class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.list = [None] * capacity
        self.capacity = capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.list)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        i = 0
        for e in self.list:
            current = e
            while current != None:
                i +=1
                current = current.next

        if i/self.capacity > .7:
            self.resize(self.capacity*2)
        elif i/self.capacity <.2:
            if self.capacity/2 < 8:
                self.resize(8)
            else:
                self.resize(self.capacity/2)
        return i/self.capacity



    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        if self.list[self.hash_index(key)] != None:
            current = self.list[self.hash_index(key)]
            while current.next != None and current.key != key:
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = HashTableEntry(key,value)
        else:
            self.list[self.hash_index(key)] = HashTableEntry(key,value)

        self.get_load_factor()

        


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # self.list[self.hash_index(key)] = None

        previous = None
        current = self.list[self.hash_index(key)]
        if current != None:
            while current.key != key and current != None:
                previous = current
                current = current.next
            if current.key == key:
                if previous != None:
                    previous.next = current.next
                else:
                    self.list[self.hash_index(key)] = current.next
            else:
                print('Key not found')
        else:
            print('Key not found')

        self.get_load_factor()


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        current = self.list[self.hash_index(key)]
        if current != None:
            while current.key != key and current.next != None:
                current = current.next
            if current.key == key:
                return current.value
            else:
                return None
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        new_list = [None]*int(new_capacity)
        for e in self.list:
            current = e
            while current != None:
                if new_list[self.hash_index(current.key)] != None:
                    cur = new_list[self.hash_index(current.key)]
                    while cur.next != None and cur.key != current.key:
                        cur = cur.next
                    if cur.key == current.key:
                        cur.value = current.value
                    else:
                        cur.next = HashTableEntry(current.key,current.value)
                else:
                    new_list[self.hash_index(current.key)] = HashTableEntry(current.key,current.value)
                current = current.next
        self.list = new_list





if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
