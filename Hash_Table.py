# HashTable class using the chaining method;
# will list elements in same bucket
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=20):
        # assigns initial capacity to 20
        self.list = []
        # O(n)
        for i in range(initial_capacity):
            self.list.append([])

    # Inserts a new item into the hash table
    # Citing source: WGU Zybooks Figure 7.8.2
    def insert(self, key, item):
        # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:  # O(n)
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Lookup items in hash table
    def search(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        # O(n)
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None  # no pair[0] matches key 0

    # Hash remove method - removes item from hash table O(1)
    def remove(self, key):
        slot = hash(key) % len(self.list)
        destination = self.list[slot]

        # If the key is found in the hash table then remove the item
        if key in destination:
            destination.remove(key)
