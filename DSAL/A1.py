class Hashtable_Linear:
    	#put collision element on next empty spot
	hash_table_num = []
	hash_table_name =[]
	def __init__(self):
		self.m = int(input("Enter size of Hash Table:"))
		
		# Initializing hash table
		for i in range(self.m):
			self.hash_table_num.append(0)
			self.hash_table_name.append(0)
		
	def hash_function(self,x):
		key = x % self.m
		return key
		
	def initialize(self,arr,names):
		for i in range(len(arr)):
			key = self.hash_function(arr[i])
			while(self.hash_table_num[key] != 0):
				key = (key + 1) % self.m
			self.hash_table_num[key] = arr[i]
			self.hash_table_name[key] = names[i]
			
	def display(self):
		print("\nKey - Value")
		for i in range(self.m):
			print(i,'-',self.hash_table_num[i],":",self.hash_table_name[i])


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
			key = self.hash_function(arr[i])
			if(self.hash_table_num[key] != 0):
				for j in range(self.m):
					key = (key + (j*j)) % self.m
					if (self.hash_table_num[key] == 0):
						self.hash_table_num[key]=arr[i]
						self.hash_table_name[key] = names[i]
						break
			else:
				self.hash_table_num[key] = arr[i]
				self.hash_table_name[key] = names[i]

	def display(self):
		print("\nKey - Value")
		for i in range(self.m):
			print(i, '-', self.hash_table_num[i], ":", self.hash_table_name[i])

			
class Hashtable_DoubleHashing:
	hash_table_num = []
	hash_table_name = []

	def __init__(self):
		self.m = int(input("Enter size of Hash Table:"))
		self.p = self.get_prime_number(self.m - 1)
		# Initializing hash table
		for i in range(self.m):
			self.hash_table_num.append(0)
			self.hash_table_name.append(0)

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

	def initialize(self, arr, names):
		for i in range(len(arr)):
			key = self.hash_function1(arr[i])
			if self.hash_table_num[key]==0:
				self.hash_table_num[key] = arr[i]
				self.hash_table_name[key] = names[i]
			else:
				# calculate the jump size using the second hash function
				jump = self.hash_function2(arr[i])
				while True:
					# calculate the next key using double hashing technique
					next_key = (key + jump) % self.m
					if self.hash_table_num[next_key] ==0:
						self.hash_table_num[next_key] = arr[i]
						self.hash_table_name[next_key] = names[i]
						break
					else:
						# update the jump size and calculate the next key
						jump += self.hash_function2(arr[i])

	def display(self):
		print("\nKey - Value")
		for i in range(self.m):
			print(i, '-', self.hash_table_num[i], ":", self.hash_table_name[i])


def main():
	# Accepting array elements
    n = int(input("Enter number of  persons:"))
    s = []
    p=[]
    g=0
    for i in range(n):
        elmt = int(input(f"Enter element ({i+1}):"))
        while(elmt<1000000000 or elmt>9999999999):
            print("Wrong Input")
            elmt = int(input(f"Enter element ({i+1}):"))
        s.append(elmt)
        
        a=(input(f"Enter name ({i+1}):"))
        p.append(a)
        
    g=int(input("Enter 1 for Linear or 2 for Double Hashing: "))
    if g == 1:
        table1 = Hashtable_Linear()
        table1.initialize(s,p)
        table1.display()
    elif g == 2:
        table2 = Hashtable_DoubleHashing()
        table2.initialize(s,p)
        table2.display()


main()
