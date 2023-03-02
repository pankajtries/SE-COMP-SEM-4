class Hashtable_Linear:
	# put collision element on next empty spot
	hash_table_num = []
	hash_table_name = []

	def __init__(self):
		self.m = int(input("Enter size of Hash Table:"))

		# Initializing hash table
		for i in range(self.m):
			self.hash_table_num.append(0)
			self.hash_table_name.append(0)

	def hash_function(self, x):
		key = x % self.m
		return key

	def initialize(self, arr, names):
		for i in range(len(arr)):
			key = self.hash_function(arr[i])
			while (self.hash_table_num[key] != 0):
				key = (key + 1) % self.m
			self.hash_table_num[key] = arr[i]
			self.hash_table_name[key] = names[i]

	def display(self):
		print("\nKey - Value")
		for i in range(self.m):
			print(i, '-', self.hash_table_num[i], ":", self.hash_table_name[i])

	def search(self, x):
		key = self.hash_function(x)
		while self.hash_table_num[key] != 0:
			if self.hash_table_num[key] == x:
				return key
			key = (key + 1) % self.m
		return None

	def insert(self, x, name):
		key = self.hash_function(x)
		while self.hash_table_num[key] != 0:
			key = (key + 1) % self.m
		self.hash_table_num[key] = x
		self.hash_table_name[key] = name
		print(f"Inserted {x} with name {name} at index {key}")

	def delete(self, x):
		key = self.search(x)
		if key is None:
			print(f"{x} not found in the hash table")
		else:
			self.hash_table_num[key] = 0
			self.hash_table_name[key] = 0
			print(f"Deleted {x} from the hash table")


class Hashtable_Quadratic:
    hash_table_num = []
    hash_table_name = []

    def __init__(self):
        self.m = int(input("Enter size of Hash Table:"))

        # Initializing hash table
        for i in range(self.m):
            self.hash_table_num.append(0)
            self.hash_table_name.append(0)

    def hash_function(self, x):
        key = x % self.m
        return key

    def initialize(self, arr, names):
        for i in range(len(arr)):
            self.insert(arr[i], names[i])

    def insert(self, num, name):
        key = self.hash_function(num)
        if self.hash_table_num[key] == 0:
            self.hash_table_num[key] = num
            self.hash_table_name[key] = name
        else:
            i = 1
            while True:
                new_key = (key + i*i) % self.m
                if self.hash_table_num[new_key] == 0:
                    self.hash_table_num[new_key] = num
                    self.hash_table_name[new_key] = name
                    break
                else:
                    i += 1

    def search(self, num):
        key = self.hash_function(num)
        if self.hash_table_num[key] == num:
            return self.hash_table_name[key]
        else:
            i = 1
            while self.hash_table_num[(key + i*i) % self.m] != 0:
                if self.hash_table_num[(key + i*i) % self.m] == num:
                    return self.hash_table_name[(key + i*i) % self.m]
                i += 1
            return None

    def delete(self, num):
        key = self.hash_function(num)
        if self.hash_table_num[key] == num:
            self.hash_table_num[key] = 0
            self.hash_table_name[key] = 0
        else:
            i = 1
            while self.hash_table_num[(key + i*i) % self.m] != 0:
                if self.hash_table_num[(key + i*i) % self.m] == num:
                    self.hash_table_num[(key + i*i) % self.m] = 0
                    self.hash_table_name[(key + i*i) % self.m] = 0
                    break
                i += 1

#Double hashing needs to be reviewed
'''
class Hashtable_DoubleHashing:
    hash_table_num = []
    hash_table_name = []

    def __init__(self):
        self.m = int(input("Enter size of Hash Table:"))
        self.p = self.get_prime_number(self.m - 1)
        # Initializing hash table
        for i in range(self.m):
            self.hash_table_num.append(None)
            self.hash_table_name.append(None)

    def get_prime_number(self, n):
        # returns the largest prime number less than n
        while True:
            if self.is_prime(n):
                return n
            n -= 1

    def is_prime(self, n):
        # checks if a number is prime
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def hash_function1(self, x):
        # first hash function
        return x % self.m

    def hash_function2(self, x):
        # second hash function
        return self.p - (x % self.p)

    def insert(self, key, name):
        i = 0
        while i < self.m:
            hash_val = (self.hash_function1(key) + i * self.hash_function2(key)) % self.m
            if self.hash_table_num[hash_val] is None:
                self.hash_table_num[hash_val] = key
                self.hash_table_name[hash_val] = name
                return
            i += 1
        print("Hashtable is full. Cannot insert new element.")

    def delete(self, key):
        i = 0
        while i < self.m:
            hash_val = (self.hash_function1(key) + i * self.hash_function2(key)) % self.m
            if self.hash_table_num[hash_val] == key:
                self.hash_table_num[hash_val] = None
                self.hash_table_name[hash_val] = None
                return
            elif self.hash_table_num[hash_val] is None:
                print("Element not found in Hashtable.")
                return
            i += 1
        print("Element not found in Hashtable.")

    def search(self, key):
        i = 0
        while i < self.m:
            hash_val = (self.hash_function1(key) + i * self.hash_function2(key)) % self.m
            if self.hash_table_num[hash_val] == key:
                return self.hash_table_name[hash_val]
            elif self.hash_table_num[hash_val] is None:
                return None
            i += 1
        return None

    def display(self):
        print("\nKey - Value")
        for i in range(self.m):
            if self.hash_table_num[i] is not None:
                print(i, '-', self.hash_table_num[i], ":", self.hash_table_name[i])
            else:
                print(i, '-', None)

'''

def main():
	table1 = Hashtable_Linear()
	table2 = Hashtable_Quadratic

	# Accepting array elements
	n = int(input("Enter number of  persons:"))
	s = []
	p=[]
	for i in range(n):
		elmt = int(input(f"Enter element ({i}):"))
		s.append(elmt)
		a=(input(f"Enter name ({i}):"))
		p.append(a)
	method=int(input("Enter 1 for Linear or 2 for Quadratic: "))
	if method == 1:
		table1.initialize(s,p)
		table1.display()
	elif method == 2:
		table2.initialize(s,p)
		table2.display()

main()


