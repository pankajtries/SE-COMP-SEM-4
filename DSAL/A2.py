

class Set:
    def __init__(self):
        self.items = []
    
    def add(self, new_element):
        if new_element not in self.items:
            self.items.append(new_element)
    
    def remove(self, element):
        if element in self.items:
            self.items.remove(element)
    
    def contains(self, element):
        return element in self.items
    
    def size(self):
        return len(self.items)
    
    def iterator(self):
        return iter(self.items)
    
    def intersection(self, other_set):
        result = Set()
        for item in self.items:
            if item in other_set.items:
                result.add(item)
        return result
    
    def union(self, other_set):
        result = Set()
        for item in self.items:
            result.add(item)
        for item in other_set.items:
            result.add(item)
        return result
    
    def difference(self, other_set):
        result = Set()
        for item in self.items:
            if item not in other_set.items:
                result.add(item)
        return result
    
    def is_subset(self, other_set):
        for item in self.items:
            if item not in other_set.items:
                return False
        return True


def main():
    # Create a new set
    s1 = Set()

    # Prompt the user to input the elements of the first set
    print("Enter the elements of the first set, separated by commas:")
    input_str = input()
    elements = input_str.split(",")
    for element in elements:
        s1.add(int(element))

    # Print the size of the set
    print("Size of set s1:", s1.size())

    # Check if an element is in the set
    print("Enter an element to check if it's in set s1:")
    input_element = int(input())
    print("s1 contains", input_element, ":", s1.contains(input_element))

    # Prompt the user to input an element to remove from the set
    print("Enter an element to remove from set s1:")
    input_element = int(input())
    s1.remove(input_element)

    # Print the size of the set again
    print("Size of set s1 after removing", input_element, ":", s1.size())

    # Create another set
    s2 = Set()

    # Prompt the user to input the elements of the second set
    print("Enter the elements of the second set, separated by commas:")
    input_str = input()
    elements = input_str.split(",")
    for element in elements:
        s2.add(int(element))

    # Compute the intersection of two sets
    s3 = s1.intersection(s2)
    print("Intersection of s1 and s2:", [item for item in s3.iterator()])

    # Compute the union of two sets
    s4 = s1.union(s2)
    print("Union of s1 and s2:", [item for item in s4.iterator()])

    # Compute the difference between two sets
    s5 = s1.difference(s2)
    print("Difference between s1 and s2:", [item for item in s5.iterator()])

    # Check if a set is a subset of another set
    s6 = Set()
    print("Enter the elements of a subset, separated by commas:")
    input_str = input()
    elements = input_str.split(",")
    for element in elements:
        s6.add(int(element))
    print("s6 is a subset of s1:", s6.is_subset(s1))

if __name__ == "__main__":
    main()
