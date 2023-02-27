class HashTable_Collision1:
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



def main():
	table = HashTable_Collision1()
	
	# Accepting array elements
	n = int(input("Enter number of  persons:"))
	s = []
	p=[]
	for i in range(n):
		elmt = int(input(f"Enter element ({i}):"))
		s.append(elmt)
		a=(input("Enter name ({i}):"))
		p.append(a)
	
	table.initialize(s,p)
	table.display()
	
	
main()
		


	
